# ⭐ Comment

```tree
comment/
├── migrations/          # Django migrations for the comment app
├── __init__.py
├── admin.py             # Admin configurations 
├── apps.py              
├── forms.py             # Django forms for CRUD operations
├── models.py            # Comment Model           
├── urls.py              # Regular (non-API) URL routes
└── views.py             # Standard Django views (non-API)
````

💻 Comment Model

The Comment Model uses Django’s content types framework (content_type, object_id, and content_object) to allow comments
to be linked to any model instance (e.g., Challenges, Events, Posts).

| Field            | Type                   | Description                                                                                       |
|------------------|------------------------|---------------------------------------------------------------------------------------------------|
| `content_type`   | `ForeignKey`           | *ForeignKey* to Django’s ContentType model. Defines the type of related model instance.           |
| `object_id`      | `PositiveIntegerField` | The primary key (ID) of the related model instance.                                               |
| `content_object` | `GenericForeignKey`    | A generic relation that links the comment to any model instance using content_type and object_id. |

Moreover, the model includes some inherited mixins:

| Mixins               | Description                                                             |
|----------------------|-------------------------------------------------------------------------|
| `LastUpdatedMixin  ` | Tracks the last modification timestamp.                                 |
| `CreatedAtMixin  `   | Stores when the category was created.                                   | 
| `CreatedByMixin  `   | *ForeignKey* to UserModel, tracks which user created the category.      |
| `ContentMixin  `     | Stores the content of the object. Minimal length value is 5 characters. |

🔧 Role Management: 

Regular authenticated users have full CRUD (Create, Read, Update, and Delete) permissions for the Comment model.
Unauthenticated user cannot create but can view the comments.


🌷 Admin Panel

The CommentAdmin class customizes how comments are managed in the Django admin panel:
- List Display: Shows content, content_object and created_by fields for quick overview.
- Ordering: Challenges are ordered by created_at in descending order (newest first). 
- Search: Allows searching by content or created_by for easier navigation.

<img width="1893" height="577" alt="image" src="https://github.com/user-attachments/assets/aff2d870-b2f5-4509-8d26-c026fbcc087b" />


#### 📣 Views:

The comment system is designed to work with multiple models (Post, Event, and Challenge) using Django’s Generic Relations.
This allows comments to be attached to different types of content without creating separate comment models for each.

🌳 CommentEditView:

This class-based view (UpdateView) allows authenticated users to edit their own comments.
The view leverages the generic relation through content_object, which points to the model instance (Post, Event, or Challenge) 
that the comment is attached to. After the comment is updated, the view redirects the user
to the related object's details page by calling self.object.content_object.get_absolute_url().
This makes the view fully generic and reusable across different models.

````python
class CommentEditView(LoginRequiredMixin, UserIsCreatorMixin, UpdateView):
    model = Comment
    form_class = CommentEditForm
    template_name = "comment/comment-edit.html"

    def get_success_url(self):
        content_object = self.object.content_object
        return content_object.get_absolute_url()
````

🌳 CommentDeleteView:

A class-based view that lets authenticated users delete their own comments. It uses a generic relation to identify the 
related object (e.g., Post, Event, Challenge) and redirects back to that object’s detail page after deletion. Access is 
restricted to the comment’s creator.

````python
class CommentDeleteView(LoginRequiredMixin, UserIsCreatorMixin, DeleteView):
    model = Comment
    template_name = "comment/comment_confirm_delete.html"

    def get_success_url(self):
        return self.object.content_object.get_absolute_url()
````

---
Next -> [Category App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/common_app.md)

--- 
Home -> [Home](https://github.com/denniesia/beaunity?tab=readme-ov-file#readme)
