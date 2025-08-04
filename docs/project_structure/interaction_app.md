# ⭐ Interaction App

```tree
interaction/
├── migrations/             # Django migrations for the category app
├── templatetags/
│ ├── init.py
│ └── interaction_tags.py   # Simple and Filter tags 
├── init.py
├── admin.py                # Admin configurations 
├── apps.py
├── models.py               # Interaction models - Like, Favourite
├── urls.py                 # Regular (non-API) URL routes
└── views.py                # Standard Django views (non-API)
````

💻 Interaction Models

Both the Like and Favourite models use Django’s Content Types Framework (content_type, object_id, and content_object).
This allows likes and favourites to be linked to any model instance (e.g., Challenges, Events, Posts) in a generic and reusable way.

✅ Advantages

- Reusability – The same Like and Favourite models can be used across multiple models without creating separate tables
for each (e.g., no need for ChallengeLike, EventLike, etc.).
- Flexibility – Easily link likes and favourites to any existing or future models.
- Less Database Duplication – Reduces redundant relationships and keeps the database cleaner.
- Easier Maintenance – Any change to the Like or Favourite logic only needs to be updated in one place.
- Extensibility – New models (e.g., Comments, Reviews) can be liked or favourited without additional migrations.

Both models inherit the InteractionBaseModel with the following fields:

| Field            | Type                   | Description                                                                                       |
|------------------|------------------------|---------------------------------------------------------------------------------------------------|
| `user`           | `ForeignKey`           | *ForeignKey* to UserModel model, tracks which user created the interaction.           |
| `content_type`   | `ForeignKey`           | *ForeignKey* to Django’s ContentType model. Defines the type of related model instance.           |
| `object_id`      | `PositiveIntegerField` | The primary key (ID) of the related model instance.                                               |
| `content_object` | `GenericForeignKey`    | A generic relation that links the interaction to any model instance using content_type and object_id. |

**🚀 Additional Features**

🔧 Role Management: 

Regular authenticated users can like and favourite instances of the models - Post, Challenge, Event. 
If an unauthenticated user try to like or favourite an instance - by manupulating the url - a redirect to the login 
page would be triggered.

🌷 Admin Panel

The LikeAdmin class and FavouriteAdmin customize how likes and favourites are managed in the Django admin panel:
- List Display: Shows user, content_object, object_id, and content_type for quick overview.
- Search: Allows searching by user for easier navigation.
  
Like:
<img width="1525" height="463" alt="image" src="https://github.com/user-attachments/assets/cae2da39-2c1d-4a8a-9ead-2e3a650b7e5c" />

Favourite:
<img width="1873" height="866" alt="image" src="https://github.com/user-attachments/assets/b7e239cc-4968-4c0e-b892-66a65b189f5f" />


📣 Views: 

`interaction/like/<str:model_name>/<int:object_id>/`- Allows authenticated users to like or unlike different types of
content (e.g., posts, categories) dynamically

- Django’s GenericForeignKey is used to link the Like model to any other model.
- The like_functionality view checks if a like already exists:
  - If not, it creates one (created=True). 
  - If it already exists, it deletes it (created=False), effectively toggling the like state.

````python
@login_required(login_url="login")
async def like_functionality(request, model_name, object_id):
    content_type = await ContentType.objects.aget(model=model_name)
    model = content_type.model_class()
    obj = await model.objects.aget(id=object_id)

    like, created = await sync_to_async(Like.objects.get_or_create)(
        user=request.user, content_type=content_type, object_id=obj.id
    )

    if not created:
        await sync_to_async(like.delete)()

    return redirect(request.META.get("HTTP_REFERER") + f"#{object_id}")
````

`interaction/favourite/<str:model_name>/<int:object_id>/` - Allows authenticated users to add or remove items
(posts, categories, etc.) to their list of favourites.

- Works similarly to the like functionality, using a GenericForeignKey in the Favourite model.

````python
@login_required(login_url="login")
async def favourite_functionality(request, model_name, object_id):
    content_type = await ContentType.objects.aget(model=model_name)
    model = content_type.model_class()
    obj = await model.objects.aget(id=object_id)

    favourite, created = await sync_to_async(Favourite.objects.get_or_create)(
        user=request.user, content_type=content_type, object_id=obj.id
    )

    if not created:
        await sync_to_async(favourite.delete)()

    return redirect(request.META.get("HTTP_REFERER", "/"))
````

`interaction/join/<str:model_name>/<int:object_id>/` - Allows users to join or leave events or challenges.

- Works directly with ManyToMany relationships between the user and the event or challenge. Similar approach to Like and
Favourite functionalities.

````python
@login_required(login_url="login")
def join_functionality(request, model_name, pk):
    user = request.user

    if model_name == "event":
        obj = get_object_or_404(Event, pk=pk)
        if user.event_attendees.filter(pk=pk).exists():
            user.event_attendees.remove(obj)
        else:
            user.event_attendees.add(obj)

    elif model_name == "challenge":
        obj = get_object_or_404(Challenge, pk=pk)
        if user.challenge_attendees.filter(pk=pk).exists():
            user.challenge_attendees.remove(obj)
        else:
            user.challenge_attendees.add(obj)

    return redirect(request.META.get("HTTP_REFERER", "/"))
````


❗Async View❗

Like & Favourite: Implemented with *asynchronous views* to efficiently handle frequent user interactions. 
Since these actions involve simple database toggling (add/remove), async improves responsiveness and scalability under 
multiple simultaneous requests.

Join: Implemented *synchronously* because it is a less frequent action involving ManyToMany relationships. 
As it usually triggers a page reload, async performance benefits are minimal.

💢 Template Tags 

The custom template tags simplify checking user interactions directly in templates:

`is_liked_by_user()` - Returns True if the given user has liked the specified object. Used to dynamically render
"liked" states in the UI.

````python
@register.filter
def is_liked_by_user(obj, user):
    content_type = ContentType.objects.get_for_model(obj)
    return Like.objects.filter(
        user=user,
        content_type=content_type,
        object_id=obj.id
    ).exists()
````

`total_likes()` - Returns the total number of likes for the given object. Helpful for displaying like counters next to 
posts, events, or challenges.

````python

@register.filter
def total_likes(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Like.objects.filter(
        content_type=content_type,
        object_id=obj.id
    ).count()

````

`is_favourited_by_user()` - Returns True if the user has marked the object as a favourite. Used for
toggling favourite indicators in templates.

````python
@register.filter
def is_favourited_by_user(obj, user):
    content_type = ContentType.objects.get_for_model(obj)
    return Favourite.objects.filter(
        user=user,
        content_type=content_type,
        object_id=obj.id
    ).exists()
````

`has_joined()` - Checks whether the user has joined an event or challenge based on the provided
model_name and object ID. Returns True if the user is a participant.

````python
@register.simple_tag
def has_joined(user, model_name, obj_id):
    if model_name == "event":
        return user.event_attendees.filter(
            pk=obj_id
        ).exists()
    elif model_name == "challenge":
        return user.challenge_attendees.filter(
            pk=obj_id
        ).exists()
    return False

````
---

Next -> [Post App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/post_app.md)

--- 
Home -> [Home](https://github.com/denniesia/beaunity/blob/main/README.md)
