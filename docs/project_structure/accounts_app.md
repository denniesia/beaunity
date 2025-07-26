# ⭐ Accounts App

```tree
accounts/
├── migrations/          # Django migrations for the accounts app
├── models/              # Custom user and profile models
│   ├── __init__.py
│   ├── app_profile.py   # User profile model (e.g., profile_pic, first_name, last_name, etc.)
│   ├── app_user.py      # Custom user model (extends AbstractBaseUser)
│   └── choices.py       # Choice constants for skin type (e.g., dry, oily, etc.)
├── __init__.py
├── admin.py             # Admin configurations w
├── api_urls.py          # API-specific URLs
├── api_views.py         # Views handling API logic (REST endpoints)
├── apps.py              # App configuration, signals registration
├── backends.py          # Custom authentication backends (email or username login)
├── decorators.py        # Custom decorators (role-based access control)
├── forms.py             # Django forms for user registration/login/update/delete
├── managers.py          # Custom model managers ( AppUserManager)
├── serializers.py       # DRF serializers for user model, login and logout
├── signals.py           # Signal handlers (auto-create profile, auto-add to group 'User')        
├── urls.py              # Regular (non-API) URL routes
└── views.py             # Standard Django views (non-API)
````



👤 User Model Implementation

The project uses a custom user model (AppUser) extending Django’s AbstractBaseUser and PermissionsMixin, alongside a 
Profile model for storing additional user information. This setup allows for a flexible and extendable authentication
and user profile system. Users can login with either email or username and password. 

AppUserModel:

| Field         | Type            | Description                                                             |
|---------------|-----------------|-------------------------------------------------------------------------|
| `email`       | `EmailField`    | Required for registration. Must be unique.                              |
| `username`    | `CharField`     | Used for login (set as USERNAME_FIELD). Must be unique.                 |
| `is_active`   | `BooleanField`  | Whether the account is active. Can be used for soft-deletion. <br/>Default is True. |
| `is_staff`    | `BooleanField`  | Determines access to Django admin site. Default is False.               |
| `date_joined` | `DateTimeField` | Timestamp of when the user registered.                                  |


Profile Model:

| Field           | Type               | Description                                                  |
|-----------------|--------------------|--------------------------------------------------------------|
| `user`          | `OneToOneField	`   | Primary key. Links to AppUser. Ensures one profile per user. |
| `profile_pic`   | `CloudinaryField`  | Optional image field stored via Cloudinary.                  |
| `first_name`    | `CharField`        | User’s first name. Optional.                                 |
| `last_name`     | `CharField`        | User’s last name. Optional.                                  |
| `date_of_birth` | `DateField`        | Used to calculate user’s age. Optional.                      |
| `location`      | `CharField`        | User’s location or city. Optional.                           |
| `bio`           | `CharField`        | Short personal bio or description.                           |
| `skin_type`     | `CharField`        | 	Skin type from SkinTypeChoices. Optional.                   |

- Model Property - `age()`- Returns user's age based on date_of_birth
- Model Method - `full_name()` - Combines and capitalizes first_name and last_name
- Custom Manager - `AppUserManager()` - provides custom user creation methods where passwords are hashed before saving the user to the database.

✅ Benefits of this structure: 
- Separates authentication concerns from profile data.
- Easy to update user info without affecting authentication flow.
- Makes use of a scalable storage backend (Cloudinary) for images.

🧩 How It Works Together:
- A user is created via the AppUser model (e.g., via registration or admin).
- A corresponding Profile is auto-created via a signal (post_save on AppUser).
- The new User is automatically - via signal - added to the *User group*, which contains the permissions.
- The Profile model is used to store and retrieve user-facing information (e.g., name, bio, avatar).

🌷 Custom User Admin

The custom User model is registered in the Django admin with:
- List display: username, email, is_staff, is_superuser
- Search: by username and email
- Custom add form: uses AppUserCreationForm
- Fieldsets: organized into credentials, personal info, and permissions
- Add user form: includes username, email, and password
- Enhanced UI: uses *django-unfold* for a better admin interface and improved user experience

This setup improves user management with a clean, tailored admin interface.

<img width="1896" height="841" alt="Screenshot_1-ezgif com-censor" src="https://github.com/user-attachments/assets/ecbdbfbc-4398-45b6-9a3a-026b46c65633" />


**🚀 Additional Features**

🎌 Signals:

The project uses Django signals to automate actions immediately after a new user is created. Two `post_save` signal handlers are connected to the `UserModel` to handle profile creation and group assignment.

-  `create_profile` - Automatically creates a `Profile` linked to the newly created user. Triggers an asynchronous task (`send_approval_email.delay`) to send an approval email, passing the user's ID and the object type `'user'`.

````python
@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_approval_email.delay(
            user_id=instance.id,
            object_type='user'
        )
````

- `add_user_to_default_group` Automatically assigns the new user to the default user group.

````python
@receiver(post_save, sender=UserModel)
def add_user_to_default_group(sender, instance,created, **kwargs):
    if created:
        user_group = Group.objects.get(name='User')
        instance.groups.add(user_group)
````

🔧 Role Management Views:

- `make_superuser()` – Grants a user the Superuser role by adding them to the corresponding group.
```python
@superuser_required
def make_superuser(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user
    group = Group.objects.get(name="Superuser")
    user.groups.add(group)
    return redirect("profile-details", pk)
```

-  `make_moderator()`  – Assigns the Moderator role (removes Organizer role if present).
```python
@superuser_required
def make_moderator(request, pk):
    """
    A moderator cannot be an organizer.
    """
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user

    if user.groups.filter(name="Organizer").exists():
        user.groups.remove(Group.objects.get(name="Organizer"))

    group = Group.objects.get(name="Moderator")
    user.groups.add(group)
    return redirect("profile-details", pk=pk)

```

-  `make_organizer()`  – Assigns the Organizer role (removes Moderator role if present).
```python
@superuser_required
def make_organizer(request, pk):
    """'
    A organizer cannot be a moderator.
    """
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user

    if user.groups.filter(name="Moderator").exists():
        user.groups.remove(Group.objects.get(name="Moderator"))

    group = Group.objects.get(name="Organizer")
    user.groups.add(group)
    return redirect("profile-details", pk=pk)
````

-  `remove_roles()`  – Clears all roles and resets the user to the default User group.
```python
@superuser_required
def remove_roles(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    user = profile.user
    user.groups.clear()
    group = Group.objects.get(name="User")
    user.groups.add(group)
    return redirect("profile-details", pk=pk)
````

🔧 Custom Decorator:

- `superuser_required()` - Checks if the user is superuser: 

````python
def superuser_required(view_func):
    return user_passes_test(lambda user: user.is_superuser)(view_func)
````

## 🌿RestFull Api Contents

**🌻 Serializers:**
 ensure the API receives the expected data and responds consistently.
- `UserSerializier()` - handles user registration data
  - Serializes the fields: username, email, and password (write-only for security).
  - Creates a new user using create_user() method, which typically hashes the password and saves the user.

- `LoginRequestSerializer()` - validates login input data.
  - Accepts username and password fields.
  - nsures both are provided for authentication.

- `LoginResponseSerializer()` - defines the format of the login response.
  - Returns access_token and refresh_token for JWT authentication. 
  - Includes a message field for any success message.

- `LogoutRequestSerializer()` - Validates logout request data.
  - Accepts a refresh_token string which is required to blacklist the token on logout.

- `LogoutResponseSerializer()` - defines the format of the logout response.
  - Returns a message field confirming logout success.


🌻 **JWT Authentication**

This project uses JSON Web Tokens (JWT) for user authentication. Upon login, the server issues:
- An access token (short-lived) to authenticate API requests.
- A refresh token (longer-lived) to get new access tokens without logging in again.

Clients send the access token with each request to access protected endpoints. When the access token expires, 
the refresh token can be used to obtain a new one. Logging out blacklists the refresh token to end the session.

✅ *JWT allows stateless, secure, and scalable authentication for REST APIs.*




🌻 **API Views**

<img width="1520" height="600" alt="image" src="https://github.com/user-attachments/assets/b913bfd3-f24e-44f4-a0c3-8f1e753e034d" />


- `/accounts/api/login/` - Authenticates a user with username and password
- `/accounts/api/logout/` -  Logs out the user by blacklisting the refresh token.
```python
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh_token")  
            token = RefreshToken(refresh_token)  
            token.blacklist()
            return Response(
                {
                    "message": "Successfully logged out.",
                },
                status=status.HTTP_200_OK,
            )
        except TokenError:
            return Response(
                {
                    "error": "Invalid or expired token.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
  ```  

- `/accounts/api/register/` - Creates a new user account, includes username, email, password
- `/accounts/api/token/refresh/` - Refreshes the JWT access token using the refresh token. Returns a new access token 
to keep the user logged in without re-entering credentials. The *TokenRefreshView* is used to build this view.

---
Next -> [Category App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/category_app.md)

--- 
Home -> [Home](https://github.com/denniesia/beaunity/blob/main/README.md)