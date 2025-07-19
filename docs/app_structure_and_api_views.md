## App Structure
[screenshot of the structure]

---

📌 **Apps**

⭐ Accounts
[screenshot of the structure]


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

- Model Property - *age* - Returns user's age based on date_of_birth
- Model Method - *full_name* - Combines and capitalizes first_name and last_name
- Custom Manager - *AppUserManager* - provides custom user creation methods where passwords are hashed before saving the user to the database.

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
- Enhanced UI: uses *django-unhold* for a better admin interface and improved user experience

This setup improves user management with a clean, tailored admin interface.

<img width="1896" height="841" alt="Screenshot_1-ezgif com-censor" src="https://github.com/user-attachments/assets/ecbdbfbc-4398-45b6-9a3a-026b46c65633" />

