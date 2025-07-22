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
  - verbose_name_plural = "Challenges"
  - permissions - 'Can approve posts', 'Can post without approval'
 

**🚀 Additional Features**

🔧 Role Management: 

Superusers and members of the Moderator group have full CRUD (Create, Read, Update, and Delete) permissions
for the Category model. Regular authenticated users can only view categories but cannot modify them unless explicitly
granted the necessary permissions.

