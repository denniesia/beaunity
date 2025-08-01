# ⭐ Category App

```tree
category/
├── migrations/          # Django migrations for the category app
├── __init__.py
├── admin.py             # Admin configurations 
├── api_urls.py          # API-specific URLs - router for ModelViewSet
├── api_views.py         # Views handling API logic (REST endpoints)
├── apps.py              
├── forms.py             # Django forms for CRUD operations
├── models.py            # Category Model
├── permissions.py       # Custom permissions for API-Views
├── serializers.py       # DRF serializers for CRUD operations and Nested Structures            
├── urls.py              # Regular (non-API) URL routes
└── views.py             # Standard Django views (non-API)
````

💻 Category Model


| Field          | Type              | Description                                                 |
|----------------|-------------------|-------------------------------------------------------------|
| `title `       | `CharField`       | Represents the title of the category. Must be unique.       |
| `image `       | `CloudinaryField` | Category image stored via Cloudinary.                       |
| `description ` | `CharField`       | Short description of the category (max 100 chars)           |
| `slug `        | `SlugField`       | Auto-generated. SEO-friendly identifier based on the title. |


| Mixins                | Description                                                        |
|-----------------------|--------------------------------------------------------------------|
| `LastUpdatedMixin  `  | Tracks the last modification timestamp.                            |
| `CreatedAtMixin  `    | Stores when the category was created.                              | 
| `CreatedByMixin  `    | *ForeignKey* to UserModel, tracks which user created the category. |

- Meta options:
  - `verbose_name_plural` = "Categories"
  - `ordering` = ["title"] (alphabetical order)

- Custom logic:
  - Automatically generates a slug from the title on save if none is provided.

````python
def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)
````

**🚀 Additional Features**

🔧 Role Management: 

Superusers and members of the Moderator group have full CRUD (Create, Read, Update, and Delete) permissions
for the Category model. Regular authenticated users can only view categories but cannot modify them unless explicitly
granted the necessary permissions.


🌷 Admin Panel

The CategoryAdmin class customizes how categories are managed in the Django admin panel:
- List Display: Shows title, description, created_by, and last_updated fields for quick overview.
- Ordering: Categories are ordered by created_at in descending order (newest first). 
- Search: Allows searching by title or created_by for easier navigation.

<img width="1874" height="653" alt="image" src="https://github.com/user-attachments/assets/81928ab7-cf5f-46dc-8554-5d60385ab7a9" />


## 🌿RestFull Api Contents

**🌻 Serializers:**
 ensure the API receives the expected data and responds consistently.

The project uses two serializers to handle Category data in different contexts:
- `CategorySimpleSerializer()` - a lightweight serializer that returns only basic category information like title and description.

````python
class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "title",
            "description"
        )
````
- `CategorySerializer()` - A detailed serializer that provides full category information.
  

````python
class CategorySerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "image",
            "description",
            "last_updated",
            "created_by",
            "created_at",
        ]
````



🌻 **API Views**

<img width="1763" height="386" alt="image" src="https://github.com/user-attachments/assets/8b787f4e-5010-4589-9554-b40f313d3add" />


- `api/#/category/` - ModelViewSet - This ModelViewSet provides full CRUD operations for the Category model.
It uses the CategorySerializer to handle serialization and ensures that the created_by field is automatically assigned to 
the authenticated user when creating a category. A custom permission class (CanAddCategory) restricts category creation to 
authorized users - members of the Moderator or Superuser Group.

```python
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [CanAddCategory]
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        user = self.request.user
        category = serializer.save(created_by=user)

```


---
Next -> [Challenge App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/challenge_app.md)

--- 
Home -> [Home](https://github.com/denniesia/beaunity/blob/main/README.md)
