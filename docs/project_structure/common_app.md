 # ⭐ Common App

The common app contains **shared utilities, abstract models, and reusable components** that are used across multiple apps 
in the project. It helps keep the codebase clean and DRY  by centralizing logic that's not 
specific to any single feature.

````tree
common/
├── migrations/          # Django migrations for the common app
├── templatetags/        # Custom template filters and tags
    ├── __init__.py
    └── has_passed.py    # Template filter to check if a datetime has passed
├── __init__.py
├── admin.py            
├── apps.py              
├── filter_mixins.py     # Mixins for filtering querysets and context data           
├── forms.py             # Shared Django forms for activities and search
├── mixins.py            # Reusable model and view mixins (e.g., timestamps, ownership)
├── models.py            # BaseActivity Model           
├── permissions.py       # Custom permission logic for DRF
├── tasks.py             # Celery tasks for background jobs (emails, updates)
├── urls.py              # Regular (non-API) URL routes
├── utils.py             # Helper functions (e.g., reminders, mark_new)
├── validators.py        # Custom validators (e.g., file size/type checks)   
└── views.py             # Standard Django views (non-API)
````

💻 BaseActivity Model

The BaseActivity model is an *abstract* base class used to define shared attributes and structure for different types
of activities in the application. It includes general fields for content, location, timing, and display preferences.
Other activity models can inherit from this base to maintain consistency and reduce code duplication across the project.

| Field          | Type              | Description                                                                                |
|----------------|-------------------|--------------------------------------------------------------------------------------------|
| `poster_image` | `CloudinaryField` | An image hosted on Cloudinary.                                                             |
| `title`        | `CharField`       | The title of the activity. Must be at least 10 characters long.                            |
| `details`      | `RichTextField`   | A rich-text description providing details about the activity.                              |
| `is_online`    | `BooleanField`    | Indicates if the activity is online (True) or in-person (False). Defaults to False         |
| `meeting_link` | `CharField`       | The meeting link for online activities. Can be blank or null.                              |
| `city`         | `CharField`       | The city where the activity takes place. Must be at least 2 characters if provided.        |
| `location`     | `CharField`       | The physical address/location of the activity. Must be at least 10 characters if provided. |
| `start_time`   | `DateTimeField`   | The start date and time of the activity.                                                   |
| `end_time`     | `DateTimeField`   | The end date and time of the activity.                                                     |
| `is_new`       | `BooleanField`    | Indicates if the activity is newly added (True). Defaults to False.                        |


**🚀 Features**

#### 🍭 Templatetags 

- The has_passed filter checks whether a given datetime has already occurred compared to the current time. This filter
is used for conditionally displaying content based on time, such as marking events or challenges as passed.

````python
@register.filter
def has_passed(obj_datetime):
    if obj_datetime:
        return obj_datetime < now()

````

#### 🍭 Filtered Mixins 

- **FilteredQuerysetMixin**

This mixin provides a method **get_filtered_queryset()** that dynamically filters a model’s queryset based on URL query
parameters. It supports filters such as:

- Archived vs. upcoming entries (based on end_time)
- City, category, difficulty level
- Online-only items
- Text search through a validated SearchForm
- Sorting by popularity, public visibility, or host
- Additional filtering for specific models like Challenge

````python
class FilteredQuerysetMixin:

    def get_filtered_queryset(self):
        current_datetime = now()
        archived = self.request.GET.get('archived', '').lower() == 'true'

        if archived:
            queryset = self.model.objects.filter(
                end_time__lt=current_datetime
            )
        else:
            queryset = self.model.objects.filter(
                end_time__gte=current_datetime
            )

        city = self.request.GET.get('city')
        category = self.request.GET.get('category')
        sort_by = self.request.GET.get('sort_by')
        online = self.request.GET.get('online')
        difficulty = self.request.GET.get('difficulty')
        query = self.request.GET.get('query')

        form = SearchForm(self.request.GET)

        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(
                    title__icontains=query)

        if city:
            queryset = queryset.filter(city=city)

        if category:
            queryset = queryset.filter(categories__title=category)

        if online:
            queryset = queryset.filter(is_online=True)

        if sort_by:
            if sort_by == 'Popularity':
                queryset = queryset.annotate(
                    popularity=Count('attendees')
                ).order_by(
                    '-popularity'
                )
            elif sort_by == 'Public':
                queryset = queryset.filter(is_public=True)
            elif sort_by == 'Hosts':
                queryset = queryset.order_by('created_by__username')


        if difficulty == 'Beginner':
            queryset = queryset.filter(difficulty='Beginner')
        elif difficulty == 'Intermediate':
            queryset = queryset.filter(difficulty='Intermediate')
        elif difficulty == 'Advanced':
            queryset = queryset.filter(difficulty='Advanced')
        elif difficulty == 'Legendary':
            queryset = queryset.filter(difficulty='Legendary')


        if self.model == Challenge:
            return queryset.filter(is_approved=True).distinct()
        return queryset.distinct()
````

- **FilteredContextMixin**

This mixin provides a method get_filtered_context() that enriches the view context with:

- Currently applied filters (to show active filter tags)
- Available cities and categories for building filter options

It ensures the frontend has all necessary metadata to reflect the current filter state 

````python
class FilteredContextMixin:
    def get_filtered_context(self, context, model):
        request = self.request
        applied_filters = {}
        query = ''

        if request.GET.get('query'):
            query = request.GET.get('query')
        if request.GET.get('city'):
            applied_filters['city'] = request.GET['city']
        if request.GET.get('category'):
            applied_filters['category'] = request.GET['category']
        if request.GET.get('sort_by'):
            applied_filters['Sorted by'] = request.GET['sort_by']
        if request.GET.get('online'):
            applied_filters['online'] = 'Online'
        if request.GET.get('archived'):
            applied_filters['archived'] = True

        #only for challenge
        if request.GET.get('difficulty'):
            applied_filters['difficulty'] = request.GET['difficulty']

        context['filter_mode'] = bool(applied_filters)
        context['applied_filters'] = applied_filters
        context['query'] = query

        context['categories'] = Category.objects.all()
        context['cities'] = model.objects.exclude(
            city=None
        ).exclude(
            city=''
        ).values_list(
            'city', flat=True
        ).distinct()

        context['model_name'] = model.__name__
        return context
````


#### 🍭 Mixins 

The following mixins are used to promote code reusability and enforce consistent behavior across multiple models and views in the project:

**View Mixins**
- *UserIsSelfMixin* - Restricts access to a view to only the user themselves. It compares the current user with the object being accessed.
- *UserIsCreatorMixin* - Grants access only if the current user is the creator of the object. Used for edit/delete permissions on user-generated content.


**Model Mixins**
- *LastUpdatedMixin* - Automatically updates a last_updated timestamp whenever the object is modified.
- *CreatedAtMixin* - Automatically stores the creation timestamp when a new object is created.
- *CreatedByMixin* - Links the object to the user who created it. Used for tracking ownership and permissions.
- *ContentMixin* - Provides a basic content field with validation. Intended for models that contain user-generated text.
- *IsApprovedMixin* - Adds a boolean is_approved field to indicate whether the object has been reviewed or approved.


#### 🍭 Forms 

**ActivityBaseForm** -  is a reusable Django ModelForm designed to handle the creation and editing of activity-related objects. 
It includes fields for content, scheduling, categorization, and location—both physical and online. It features:
- File upload via Cloudinary with validation and styling.
- Rich text editing using CKEditor.
- Input sanitization and validation (e.g. minimum character length for details).
- Custom widgets for styling and improved user experience.

**SearchForm** - A simple search form used to capture text-based queries. It provides a styled input field and is used 
for filtering results across the platform.


#### 🍭 Validators

**CloudinaryExtensionandSizeValidator** - This is a custom file validator used to ensure uploaded files meet specific type and size 
requirements. It is:
- Decorated with @deconstructible so it can be used in Django migrations.
- Designed to restrict file types to .jpg, .jpeg, .png, .gif, .pdf, and .mp4.
- Enforces a maximum file size limit (default: 5MB).
- Compatible with Django forms and models, especially useful for Cloudinary uploads.

````python
@deconstructible
class CloudinaryExtensionandSizeValidator:
    def __init__(self, max_size_mb=5):
        self.max_size_mb = max_size_mb

    @property
    def allowed_extensions(self):
        return [".jpg", ".jpeg", ".png", ".gif", ".pdf", ".mp4"]

    def __call__(self, file):
        if isinstance(file, CloudinaryResource):
            return

        if file.size > self.max_size_mb * 1024 * 1024:
            raise ValidationError(f"File size must be under {self.max_size_mb} MB.")

        extension = os.path.splitext(file.name)[1].lower()

        if extension not in self.allowed_extensions:
            raise ValidationError(f"Unsupported file type: {extension}.")
````


#### 🍭 Shared Tasks

These tasks are executed asynchronously using **Celery**, allowing time-consuming operations like sending emails or
updating data to run in the background without blocking the user experience.

**send_approval_email** - Sends an approval or welcome email to a user based on the type of object (e.g., post, challenge, or user account).
It dynamically selects the subject and message template and uses Django’s send_mail function to deliver the email.

````python
@shared_task()
def send_approval_email(user_id, object_type, object_title=None):
    User = get_user_model()
    user = User.objects.get(id=user_id)

    email_templates = {
        'post': {
            'subject': 'Your post has been approved',
            'message': f'Hi {user.username},\n\nYour post "{object_title}" has been approved!'
        },
        'challenge': {
            'subject': 'Challenge submission approved',
            'message': f'Hi {user.username},\n\nYour challenge "{object_title}" is now live!'
        },
        'user': {
            'subject': "Welcome to beaunity!",
            'message': f"Hi {user.username},\n\nWe're excited to have you on board."
        }
    }

    send_mail(
        subject=email_templates[object_type]['subject'],
        message=email_templates[object_type]['message'],
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=True
    )
````
The approval email related to new account creation is triggered by a signal in the accounts app.

```python
#beaunity/accounts/signals.py

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_approval_email.delay(
            user_id=instance.id,
            object_type='user'
        )
```
Approval emails for posts and challenges are triggered by a view in the common app.

````python
#beaunity/common/views.py

@login_required
def approve_instance(request, model_class, pk: int, content_type:str, permission_required: str, redirect_approved, redirect_fallback):
    instance = get_object_or_404(model_class, pk=pk)

    if request.user.has_perm(permission_required):
        instance.is_approved = True
        instance.save()
        send_approval_email.delay(
            user_id=instance.created_by.id,
            object_type=content_type,
            object_title=instance.title
        )
        return redirect(redirect_approved)

    return redirect(redirect_fallback)
````

**send_reminders** - Sends reminder emails to users who are attending upcoming events or challenges.
This task loops through each object’s attendees and dispatches personalized reminder emails using a helper function.
It is scheduled via Celery Beat to run daily at 8:00 AM, ensuring that users are notified two days before their upcoming
activity.

````python
@shared_task
def send_reminders():
    events = get_upcoming_events()
    challenges = get_upcoming_challenges()

    for event in events:
        for user in event.attendees.all():
            send_reminder_email(user, event.title, event.start_time, "event")

    for challenge in challenges:
        for user in challenge.attendees.all():
            send_reminder_email(user, challenge.title, challenge.start_time, "challenge")
````
````python
#beaunity/celery.py

app.conf.beat_schedule = {
    'send-reminders-every-morning' : {
        'task': 'beaunity.common.tasks.send_reminders',
        'schedule':  crontab(hour=8, minute=0),
       
    },
    ... 
 ````   


**update_is_new_status** - Automatically updates the is_new status for events and challenges based on business logic defined in 
the mark_new() helper. This task helps keep the content up to date, likely for UI indicators or filtering.It is scheduled 
via Celery Beat to run daily at midnight (00:00) to ensure the "new" status is consistently up to date

````python
@shared_task
def update_is_new_status():
    mark_new(Event)
    mark_new(Challenge)
````

````python
#beaunity/celery.py

app.conf.beat_schedule = {

    'update_is_new_status_daily': {
        'task': 'beaunity.common.tasks.update_is_new_status',
        'schedule': crontab(hour=0, minute=0),
      
    }
}
````


#### 🍭 Utility Functions for Scheduling & Notifications

These helper functions support background tasks like reminders and content tagging by automating date-based logic.
They are also triggered by **Celery tasks** to keep users informed and engaged without manual intervention.

**mark_new(model)** - Marks recently created objects as “new” by setting their is_new field to True if they were created within the past week.
Used for visually highlighting new content in the UI.

````python
def mark_new(model):
    current_date = now()
    week_ago = current_date - timedelta(weeks=1)

    model.objects.filter(
        created_at__range=(week_ago, current_date)
    ).update(is_new=True)
````

**get_upcoming_events()** and **get_upcoming_events()** - Fetch events or challenges that are scheduled to start exactly two days from today.
Used with the celery **shared tasks** for sending timely reminders to participants.

````python
def get_upcoming_events():
    two_days_later = now().date() + timedelta(days=2)
    
    return Event.objects.filter(
        start_time__date=two_days_later
    )


def get_upcoming_challenges():
    two_days_later = now().date() + timedelta(days=2)
    
    return Challenge.objects.filter(
        start_time__date=two_days_later
    )
````


**send_reminder_email(user, title, start_time, item_type)** - Composes and sends a personalized reminder email to a user about an upcoming event or challenge, including the name and date.
The subject and message are customized based on the content type.

````python
def send_reminder_email(user, title, start_time, item_type):
    start_time_str = start_time.strftime('%Y-%m-%d %H:%M')

    if item_type == "event":
        subject = f"BEAUNITY Reminder: {title} is in 2 days!"
        message = (
            f"Hello {user.username},\n\n"
            f"Just a reminder that the event '{title}' starts in 2 days on - {start_time_str}.\n"
            f"See you there!"
        )
    elif item_type == 'challenge':
        subject = f"BEAUNITY Reminder: Challenge - {title} - starts in 2 days!"
        message = (
            f"Hello {user.username},\n\n"
            f"Just a reminder that the challenge '{title}' starts in 2 days on - {start_time_str}.\n"
            f"Get ready to smash it!"
        )

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=True,
    )
````







