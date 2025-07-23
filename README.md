# 🩷 Beaunity – Empowering Beauty Through Community

Beaunity is a forum-like platform where users can create, discover, and participate in challenges, discussions and events — both online and offline. The app brings together beauty enthusiasts, professionals, and brands to share their creativity and knowledge through interactive experiences. Whether you're building a skincare routine, exploring makeup trends, or hosting a beauty workshop, Beaunity helps you grow individually while connecting with a supportive community.

---

## 💖 The Vision

To empower individuals to embrace their unique selves through collaboration, creativity, and meaningful connections.

---

### Contents
- [Project Setup](docs/project_setup.md)
- [Exploring beaunity](docs/exploring_beaunity.md)
- [App Structure & Api Views](docs/app_structure_and_api_views.md)
- [Role Management](docs/role_management)


---

## Core Features

- 🧴 **User-Generated Challenges**  
  Create challenges with images, meeting links, and categorize them with predefined tags for easy discovery.

- 🗓️ **Host Online & Offline Events**  
  Organize workshops, tutorials, or in-person meetups with built-in scheduling and management tools.

- 💬 **Engage Through Comments & Likes**  
  Interact with other users by giving feedback, encouragement, and inspiration.

- 🔍 **Discover by Category**  
  Browse challenges and events by interests—ranging from skincare and makeup to wellness and self-care.

- 📩 **Approval Workflow**  
  Admins and moderators review and approve or reject submitted challenges and posts before they go live.

- 👩‍💼 **Role-Based Permissions**  
  Access and functionality are managed based on user roles, such as admins, moderators, and regular users.

- 🌍 **Community-Driven**  
  Explore challenges filtered by category or location, fostering interaction, learning, and community building.

---

## 🛠️ Tools and Technologies: 

Beaunity leverages a modern Python and Django-based tech stack to deliver a robust, scalable, and feature-rich web application. Below is an overview of the main tools and libraries used

### Backend Framework

- Django (5.2.2) – A high-level Python web framework for rapid development and clean design.
- Django REST Framework (3.16.0) – For building RESTful APIs.
- Django Allauth (65.9.0) – Handles authentication, registration, social logins, and account management.
- SimpleJWT (djangorestframework-simplejwt) – JWT-based authentication for secure API access.

### Task Queue & Asynchronous Processing

- Celery (5.5.3) – Distributed task queue for handling asynchronous background tasks.
- Django Celery Beat (2.8.1) – Periodic task scheduling for Celery.
- Redis (6.2.0) – Message broker and caching backend for Celery.

### Database & Storage

- PostgreSQL (psycopg2==2.9.10) – Relational database for structured data storage.
- psycopg2 – PostgreSQL adapter for Python
- Cloudinary (1.44.0) – Cloud-based image and video storage.
- Django Cloudinary Storage (0.3.0) – Cloudinary integration for Django.

### Admin & Rich Content Management

- Django CKEditor (6.7.3) – Rich-text editor for content creation.
- Django Unfold (0.60.0) – Modern Django admin theme.
- Django Tailwind (4.0.1) – TailwindCSS integration for custom frontend styling.

### API Documentation
- DRF Spectacular (0.28.0) – Generates OpenAPI 3-compliant API documentation.

### Security 
- Python Decouple (3.8) – Securely manages environment variables and settings.

### Social Authentication

- Social Auth App Django (5.5.0) – Social authentication (Google).
- OAuthlib & Requests-OAuthlib – OAuth2 support for secure social logins.

### Utilities & Development Tools

- Black (25.1.0) – Code formatting for Python.
- Isort (6.0.1) – Organizes imports automatically.
- Bleach (6.2.0) – HTML sanitization for security.

### Other Notable Libraries
- Pillow (11.2.1) – Image processing.
- Python Slugify (8.0.4) – Creates clean URL slugs.







