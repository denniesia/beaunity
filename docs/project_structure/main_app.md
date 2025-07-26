 # ⭐ Main App

The `main` app is responsible for rendering the core pages of the project, including the **landing page**,
**about page**, and **dashboard**.

````tree
main/
├── migrations/          # Django migrations for the main app
├── __init__.py
├── admin.py            
├── api_urls.py          # URL routes for API endpoints related to main pages  
├── api_views.py         # API views for serving JSON responses (e.g. dashboard data)   
├── apps.py               
├── forms.py             # Django forms used in main pages (e.g. contact form)
├── models.py                 
├── urls.py              # Regular (non-API) URL routes
└── views.py             # Standard Django views (non-API)
````


## 🌿RestFull Api Contents

🌻 **API Views**

<img width="1551" height="734" alt="image" src="https://github.com/user-attachments/assets/443aa368-3d37-491f-995c-703fb95d8682" />


- `api/#/search/`  -This API endpoint allows users to perform a global search across multiple models (Post, Category,
Event, Challenge, and User) using a single query string. It supports simple case-insensitive matching on titles and usernames.

````python
@extend_schema(
    tags=['search'],
    summary="Global Search endpoint",
    description="Search across posts, categories, events, challenges, and users by query string",
    parameters=[
        OpenApiParameter(
            name="q",
            description="Search",
            required=False,
            type=str,
            location=OpenApiParameter.QUERY # /endpoint/?param=value
        )
    ],
)
@api_view(['GET'])
def global_search(request):
    query = request.GET.get('q', '')

    if not query:
        return Response(
            {
                "detail": "Query parameter 'q' is required."
            },
            status=HTTPStatus.BAD_REQUEST
        )


    posts = Post.objects.filter(
        title__icontains=query
    )
    posts_data = PostSerializer(posts, many=True).data

    categories = Category.objects.filter(
        title__icontains=query
    )
    categories_data = CategorySerializer(categories, many=True).data

    events = Event.objects.filter(
        title__icontains=query
    )
    events_data = EventSerializer(events, many=True).data

    challenges = Challenge.objects.filter(
        title__icontains=query
    )
    challenges_data = ChallengeSerializer(challenges, many=True).data


    users = UserModel.objects.filter(
        username__icontains=query
    )
    users_data = UserSerializer(users, many=True).data

    return Response(
        {
            'posts': posts_data,
            'categories': categories_data,
            'events': events_data,
            'challenges': challenges_data,
            'users': users_data,
        }
    )
````

Next -> [Post App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/post_app.md)

--- 
Home -> [Home](https://github.com/denniesia/beaunity/blob/main/README.md
