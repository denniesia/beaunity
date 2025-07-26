# ⭐ Post App

```tree
post/
├── migrations/          # Django migrations for the post app
├── __init__.py
├── admin.py             # Admin configurations 
├── api_urls.py          # API-specific URLs - router for ModelViewSet
├── api_views.py         # Views handling API logic (REST endpoints)
├── apps.py              
├── forms.py             # Django forms for CRUD operations
├── models.py            # Post Model
├── serializers.py       # DRF serializers for CRUD operations             
├── urls.py              # Regular (non-API) URL routes
└── views.py             # Standard Django views (non-API)
````

💻 Post Model

| Field        | Type              | Description                                                               |
|--------------|-------------------|---------------------------------------------------------------------------|
| `banner`     | `URLField`        | An Url image.                                                             |
| `title`      | `CharField`       | The title of the post. Must be at least 5 characters long.                |
| `category`   | `ForeignKey`      | *ForeignKey* to Category Model, tracks what category the post belongs to. |
| `comments`   | `GenericRelation` | *Generic relation* to Comment Model for tracking comments.                |
| `likes`      | `GenericRelation` | *Generic relation* to Like Model for tracking likes.                      |
| `favourites` | `GenericRelation` | *Generic relation* to Favourite Model for tracking favourites.            |

Moreover, the model includes additional mixins:

| Mixins               | Description                                                          |
|----------------------|----------------------------------------------------------------------|
| `LastUpdatedMixin  ` | Tracks the last modification timestamp.                              |
| `CreatedAtMixin  `   | Stores when the post was created.                                    | 
| `CreatedByMixin  `   | *ForeignKey* to UserModel, tracks which user created the post.       |
| `IsApprovedMixin  `  | Defines if the post has been approved. Default is False.             |
| `ContentMixin  `     | Defines the content of the post. Must be at least 5 characters long. |


- Meta options:
  - `verbose_name_plural` = "Challenges"
  - `permissions` - 'Can approve posts', 'Can post without approval'
 

**🚀 Additional Features**

🔧 Role Management: 

Regular authenticated users have full CRUD (Create, Read, Update, and Delete) permissions for the Post model.
After a post is created, it must be approved by a member of the Superuser group or the Moderator group before it becomes publicly visible. 
Unauthenticated user can see a full list of the posted post, but cannot comment until logged in. 



🌷 Admin Panel

<img width="1884" height="880" alt="image" src="https://github.com/user-attachments/assets/1fe69b44-74ef-46e7-b324-ea892d1e0a6d" />


The **PostAdmin** class customizes how **posts** are managed in the Django admin panel:
- List Display: Shows title, is_approved, created_at, category and created_by fields for quick overview.
- Ordering: **Post** are ordered by created_at in descending order (newest first). 
- Search: Allows searching by title or created_by__username for easier navigation.

## 🌿RestFull Api Contents

**🌻 Serializers:**
ensure the API receives the expected data and responds consistently.

The Model has only one serializer:
- `PostSerializer()` - is used to serialize and deserialize Post objects for the API.

```python
class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='title'
    )
    created_by = UserSerializer(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = [
            "banner", "title",
            "content", "category",
            "last_updated", "created_by",
            "created_at"
        ]
```


🌻 **API Views** 

<img width="1515" height="404" alt="image" src="https://github.com/user-attachments/assets/2ebe5dad-3ce1-4c2d-a7b0-615b0d16ab33" />


- `api/#/post/` - This ModelViewSet provides full CRUD operations for the **Post** model. The logged-in user is 
automatically set as the created_by field when creating a post. The category field accepts the title of an existing 
category (slug-based lookup). If the user has the permission to post without approval - belongs to the Moderator's or the 
Superuser's group - the post is automatically approved and posted.
````python

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsCreatorOrSuperuser()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        user = self.request.user
        post = serializer.save(created_by=user)

        if user.has_perm('post.can_post_without_approval'):
            post.is_approved = True
            post.save()
````

--- 
Home -> [Home](https://github.com/denniesia/beaunity/blob/main/README.md)
