## Project Structure

```tree
beauinty
    ├── accounts/
    ├── category/
    ├── challenge/
    ├── comment/
    ├── common/            # Shared utilities (abstract models, mixins, helpers).
    ├── event/
    ├── interaction/
    ├── main/              # General views - about page, landing page, dashboard
    ├── post/              
    └── scripts/           # Populating data scripts
├── __init__.py
├── asgi.py
├── celery.py              # Celery configuration for background tasks.
├── settings.py            # Django settings and configurations.
├── urls.py                # Global URL routing.
├── wsgi.py
├── docs/                  # Documentation and reports for the project.
└── templates/             # Global Django templates folder (with per-app subfolders).
    ├── accounts/
    ├── category/
    ├── challenge/
    ├── comment/
    ├── common/
    ├── event/
    ├── interaction/
    ├── main/
    └── post/
├── tests/                  # Test suites
├── theme/                  # Styling/layout assets (Tailwind)
├── env.template            # Sample environment variables.
├── .gitignore
├── Dockerfile              # Docker build instructions
├── Procfile                # Process declaration (Railway)
├── README.md               # Project overview and setup instructions
├── docker-compose.yml      # Container configuration
├── manage.py               # Django command-line utility
├── requirements.txt        # Python dependencies
```


---

📌 **Apps**

- [Accounts App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/accounts_app.md)
- [Category App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/category_app.md)
- [Challenge App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/challenge_app.md)
- [Comment App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/comment_app.md)
- [Common App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/common_app.md)
- [Event App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/event_app.md)
- [Interaction App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/interaction_app.md)
- [Main App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/main_app.md)
- [Post App](https://github.com/denniesia/beaunity/blob/main/docs/project_structure/post_app.md)
