
⭐ Category

```tree
category/
├── migrations/          # Django migrations for the category app
├── __init__.py
├── admin.py             # Admin configurations w
├── api_urls.py          # API-specific URLs
├── api_views.py         # Views handling API logic (REST endpoints)
├── apps.py              # App configuration, signals registration
├── forms.py             # Django forms for user registration/login/update/delete
├── models.py            
├── permissions.py         
├── serializers.py       # DRF serializers for user model, login and logout
├── tests.py             
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
  - verbose_name_plural = "Categories"
  - ordering = ["title"] (alphabetical order)

- Custom logic:
  - Automatically generates a slug from the title on save if none is provided.

````python
def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.title)
      super().save(*args, **kwargs)
````

**🚀 Additional Features**

🔧 Role Management Views: 

Superusers and members of the Moderator group have full CRUD (Create, Read, Update, and Delete) permissions
for the Category model. Regular authenticated users can only view categories but cannot modify them unless explicitly
granted the necessary permissions. 


🌷 Admin Panel

The CategoryAdmin class customizes how categories are managed in the Django admin panel:
- List Display: Shows title, description, created_by, and last_updated fields for quick overview.
- Ordering: Categories are ordered by created_at in descending order (newest first). 
- Search: Allows searching by title or created_by for easier navigation.

## 🌿RestFull Api Contents

**🌻 Serializers:**
 ensure the API receives the expected data and responds consistently.

The project uses two serializers to handle Category data in different contexts:
- CategorySimpleSerializer - a lightweight serializer that returns only basic category information like title and description.

- A detailed serializer that provides full category information, including metadata:
  - id – The unique identifier of the category.
  - title – The category name.
  - image – The category image (Cloudinary-hosted).
  - description – A short description of the category.
  - last_updated (read-only) – Timestamp of the last update.
  - created_by (read-only) – User who created the category (nested UserSerializer).
  - created_at (read-only) – Timestamp when the category was created.

🌻 **API Views**

- api/#/category/ - ModelViewSet - This ModelViewSet provides full CRUD operations for the Category model.
It uses the CategorySerializer to handle serialization and ensures that the created_by field is automatically assigned to 
the authenticated user when creating a category. A custom permission class (CanAddCategory) restricts category creation to 
authorized users - members of the Moderator or Superuser Group.