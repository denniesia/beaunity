# ⭐ Challenge

```tree
challenge/
├── migrations/          # Django migrations for the challenge app
├── __init__.py
├── admin.py             # Admin configurations 
├── api_urls.py          # API-specific URLs - router for ModelViewSet
├── api_views.py         # Views handling API logic (REST endpoints)
├── apps.py              
├── choices.py           # Choice constants for difficulty level (e.g., beginner, intermediate, etc.)
├── forms.py             # Django forms for CRUD operations
├── models.py            # Challenge Model
├── permissions.py       # Custom permissions for API-Views
├── serializers.py       # DRF serializers for CRUD operations             
├── urls.py              # Regular (non-API) URL routes
└── views.py             # Standard Django views (non-API)
````

💻 Challenge Model

The Challenge Model inherits the BaseActivity abstract class, which contains:

| Field          | Type              | Description                                                                                |
|----------------|-------------------|--------------------------------------------------------------------------------------------|
| `poster_image` | `CloudinaryField` | An image hosted on Cloudinary.                                                             |
| `title`        | `CharField`       | The title of the challenge. Must be at least 10 characters long.                           |
| `details`      | `RichTextField`   | A rich-text description providing details about the challenge.                             |
| `is_online`    | `BooleanField`    | Indicates if the activity is online (True) or in-person (False). Defaults to False         |
| `meeting_link` | `CharField`       | The meeting link for online activities. Can be blank or null.                              |
| `city`         | `CharField`       | The city where the activity takes place. Must be at least 2 characters if provided.        |
| `location`     | `CharField`       | The physical address/location of the activity. Must be at least 10 characters if provided. |
| `start_time`   | `DateTimeField`   | The start date and time of the challenge.                                                  |
| `end_time`     | `DateTimeField`   | The end date and time of the activity.                                                     |
| `is_new`       | `BooleanField`    | 	Indicates if the activity is newly added (True). Defaults to False.                       |

Moreover, the model includes additional fields:

| Field        | Type               | Description                                                                                                            |
|--------------|--------------------|------------------------------------------------------------------------------------------------------------------------|
| `difficulty` | `CharField `       | Defines the challenge difficulty level. Choices are Beginner, Intermediate, Advanced, Legendary. Defaults to Beginner. |
| `categories` | `ManyToManyField ` | *ManyToManyField* to Category Model. Links the challenge to one or more categories.                                    |
| `attendees`  | `ManyToManyField ` | *ManyToManyField* to UserModel. Users who have joined the challenge. Can be empty.                                     |
| `likes`      | `GenericRelation ` | *Generic relation* to Like Model for tracking likes.                                                                   |
| `comments `  | `GenericRelation ` | *Generic relation* to Comment Model for tracking comments.                                                             |

And some inherited Mixins:

| Mixins                | Description                                                        |
|-----------------------|--------------------------------------------------------------------|
| `LastUpdatedMixin  `  | Tracks the last modification timestamp.                            |
| `CreatedAtMixin  `    | Stores when the category was created.                              | 
| `CreatedByMixin  `    | *ForeignKey* to UserModel, tracks which user created the category. |
| `IsApprovedMixin  `    | Defines if the object has been approved. Default is False.         |

- Meta options:
  - verbose_name_plural = "Challenges"
  - permissions - 'Can approve challenge'
  - properties:
    - progress - Calculates the progress of the challenge in percentage (0% before start, 100% after end.
    - duration_in_weeks - Returns the total challenge duration in weeks, rounded up.


🔧 Role Management: 

Regular authenticated users have full CRUD (Create, Read, Update, and Delete) permissions for the Challenge model.
After a challenge is created, it must be approved by a member of the Superuser group or the Moderator group before it becomes publicly visible. 
Unauthenticated user cannot see a full list of the posted challenges.


🌷 Admin Panel

The ChallengeAdmin class customizes how challenges are managed in the Django admin panel:
- List Display: Shows title, created_by, created_at, start_time and end_time fields for quick overview.
- Ordering: Challenges are ordered by created_at in descending order (newest first). 
- Search: Allows searching by title or created_by for easier navigation.

<img width="1878" height="523" alt="image" src="https://github.com/user-attachments/assets/19e403ff-8ed2-44e2-91ca-e96c56e3519e" />


## 🌿RestFull Api Contents

**🌻 Serializers:**
ensure the API receives the expected data and responds consistently.

The project uses two serializers to handle Challenge data in different contexts:
- ChallengeSerializer -  is used for retrieving and displaying challenge data in a structured JSON format. 
It is based on the Challenge model and includes related data such as categories and the user who created the challenge. 
  - Validation:
    - validate_data method - ensures that the challenge description contains at least 100 characters of plain text 
    (HTML tags are stripped before validation using bleach).
    - validate_poster_image method - Validates the image using a custom CloudinaryExtensionandSizeValidator to check 
    for allowed file types and size limits.
    - validate method - ensures the end_time is after the start_time.
    
````python
class ChallengeSerializer(serializers.ModelSerializer):
    categories = CategorySimpleSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Challenge
        fields = [
            'poster_image', 'title', 'details',
            'is_online', 'city', 'location', 'meeting_link',
            'start_time', 'end_time', 'categories',
            'difficulty', "last_updated", "created_by", "created_at"
        ]

    def validate_details(self, value):
        plain_text = bleach.clean(value, tags=[], strip=True)
        if len(plain_text.strip()) < 100:
            raise serializers.ValidationError("Description must be at least 100 characters.")
        return cleaned_value

    def validate_poster_image(self, image):
        try:
            CloudinaryExtensionandSizeValidator()(image)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(str(e))
        return image

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError(
              {
                "end_time": "End time must be after start time."
              }
            )
        return data
````

- ChallengeCreateSerializer - extends ChallengeSerializer and is used specifically for creating new challenges.
````python
class ChallengeCreateSerializer(ChallengeSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='title',
        many=True,
    )
````


🌻 **API Views**
<img width="1538" height="413" alt="image" src="https://github.com/user-attachments/assets/2ec09c42-fa16-4c3a-8140-43a33fadec8a" />


- api/#/challenge/ - This ModelViewSet provides full CRUD operations for the Challenge model.
It uses ChallengeCreateSerializer for creating challenges (allows category selection by slug) and ChallengeSerializer 
for reading and other operations. The logged-in user is automatically set as the created_by field when creating a challenge.

````python
class ChallengeViewSet(ModelViewSet):
    queryset = Challenge.objects.filter(
        is_approved=True
    ).select_related(
        "created_by"
    ).prefetch_related(
        "categories", "attendees"
    )

    def get_serializer_class(self):
        if self.action == 'create':
            return ChallengeCreateSerializer
        return ChallengeSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsCreator()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        user = self.request.user
        challenge = serializer.save(created_by=user)

        if user.has_perm('challenge.can_post_without_approval'):
            challenge.is_approved = True
            challenge.save()

````
