# ⭐ Event App

```tree
event/
├── migrations/          # Django migrations for the event app
├── __init__.py
├── admin.py             # Admin configurations 
├── api_urls.py          # API-specific URLs - router for ModelViewSet
├── api_views.py         # Views handling API logic (REST endpoints)
├── apps.py              
├── forms.py             # Django forms for CRUD operations
├── mixins.py            # EventValidationMixin and PublicFieldMixin  
├── models.py            # Event Model
├── permissions.py       # Custom permissions for API-Views
├── serializers.py       # DRF serializers for CRUD operations             
├── urls.py              # Regular (non-API) URL routes
└── views.py             # Standard Django views (non-API)
````

💻 Event Model

The Event Model inherits the BaseActivity abstract class, which contains:

| Field          | Type              | Description                                                                               |
|----------------|-------------------|-------------------------------------------------------------------------------------------|
| `poster_image` | `CloudinaryField` | An image hosted on Cloudinary.                                                            |
| `title`        | `CharField`       | The title of the challenge. Must be at least 10 characters long.                          |
| `details`      | `RichTextField`   | A rich-text description providing details about the challenge.                            |
| `is_online`    | `BooleanField`    | Indicates if the activity is online (True) or in-person (False). Defaults to False        |
| `meeting_link` | `CharField`       | The meeting link for online activities. Can be blank or null.                             |
| `city`         | `CharField`       | The city where the activity takes place. Must be at least 2 characters if provided.       |
| `location`     | `CharField`       | The physical address/location of the activity. Must be at least 10 characters if provided. |
| `start_time`   | `DateTimeField`   | The start date and time of the challenge.                                                 |
| `end_time`     | `DateTimeField`   | The end date and time of the activity.                                                    |
| `is_new`       | `BooleanField`    | Indicates if the activity is newly added (True). Defaults to False.                       |

Moreover, the model includes additional fields:

| Field        | Type               | Description                                                                         |
|--------------|--------------------|-------------------------------------------------------------------------------------|
| `is_public`  | `CharField `       | Defines if the event is public. Defaults to Beginner. Default is True.              |
| `categories` | `ManyToManyField ` | *ManyToManyField* to Category Model. Links the challenge to one or more categories. |
| `attendees`  | `ManyToManyField ` | *ManyToManyField* to UserModel. Users who have joined the challenge. Can be empty.  |
| `likes`      | `GenericRelation ` | *Generic relation* to Like Model for tracking likes.                                |
| `comments `  | `GenericRelation ` | *Generic relation* to Comment Model for tracking comments.                          |
| `favourites` | `GenericRelation`  | *Generic relation* to Favourite Model for tracking favourites.            |

And some inherited Mixins:

| Mixins                | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| `LastUpdatedMixin  `  | Tracks the last modification timestamp.                         |
| `CreatedAtMixin  `    | Stores when the event was created.                              | 
| `CreatedByMixin  `    | *ForeignKey* to UserModel, tracks which user created the event. |


- Meta options:
  - verbose_name_plural = "Events"

*🚀 Additional Features**

🔧 Role Management: 

Superusers and members of the Organizer group have full CRUD (Create, Read, Update, and Delete) permissions
for the Event model. Regular authenticated users can view, join, like events and add them to the favourites.
Unauthenticated user cannot see a full list of the posted events.


🌷 Admin Panel

The EventAdmin class customizes how events are managed in the Django admin panel:
- List Display: Shows title, created_by, created_at, start_time and end_time fields for quick overview.
- Ordering: Events are ordered by created_at in descending order (newest first). 
- Search: Allows searching by title or created_by for easier navigation.

<img width="1886" height="653" alt="image" src="https://github.com/user-attachments/assets/54d210d3-9c5d-4ad5-bda8-626a8c24a1cc" />

## 🌿RestFull Api Contents

**🌻 Serializers:**
ensure the API receives the expected data and responds consistently.


The project uses two serializers to handle Event data in different contexts:
- EventSerializer -  is used for retrieving and displaying challenge data in a structured JSON format. 
It is based on the Event model and includes related data such as categories and the user who created the challenge. 
  - Validations:
    - validate_details method - ensures that the event details contains at least 100 characters of plain text 
    (HTML tags are stripped before validation using bleach).
    - validate_poster_image method - Validates the image is using a custom CloudinaryExtensionandSizeValidator to check 
    for allowed file types and size limits.
    - validate method - ensures the end_time is after the start_time. 
    - validate_time method - ensures the end_time is after the start_time.

````python
class EventSerializer(serializers.ModelSerializer):
    categories = CategorySimpleSerializer(many=True, read_only=True)
    created_by = UserSerializer(read_only=True)
    is_public = serializers.BooleanField(read_only=True)
    last_updated = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Event
        fields = [
            'poster_image', 'title', 'details',
            'is_online', 'is_public', 'city', 'location',
            'meeting_link', 'start_time', 'end_time', 'categories',
            "last_updated", "created_by", "created_at", 'is_public'
        ]

    def validate_details(self, value):
        cleaned_value = bleach.clean(value, tags=[], strip=True)
        if len(plain_text.strip()) < 100:
            raise serializers.ValidationError("Description must be at least 100 characters.")
        return cleaned_value

    def validate_poster_image(self, image):
        CloudinaryExtensionandSizeValidator()(image)
        return image
    
    def validate_time(self, data):
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError(
                {"end_time": "End time must be after start time."}
            )
        return data
````

- EventCreateSerializer - extends EventSerializer and is used specifically for creating new events.
````python
class EventCreateSerializer(EventSerializer):
    categories = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='title',
        many=True,
    )
````


🌻 **API Views**

<img width="1525" height="382" alt="image" src="https://github.com/user-attachments/assets/9e783d1a-b697-42ae-934f-de0e440af9f2" />


- api/#/event/ - This ModelViewSet provides full CRUD operations for the Event model.
It uses EventCreateSerializer for creating challenges (allows category selection by slug) and EventSerializer 
for reading and other operations. When a logged-in user with the appropriate permission creates an event, they are 
automatically set as the 'created_by' user.

````python
class EventViewSet(ModelViewSet):
    queryset = Event.objects.order_by('-created_at')

    def get_serializer_class(self):
        if self.action == 'create':
            return EventCreateSerializer
        return EventSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsCreator()]
        elif self.action == 'create':
            return [IsAuthenticated(), CanAddEvent()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        user = self.request.user
        event = serializer.save(created_by=user)
````

---
Next -> [Interaction App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/interaction_app.md)

--- 
Home -> [Home](https://github.com/denniesia/beaunity/blob/main/README.md
