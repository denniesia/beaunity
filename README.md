# 🩷 Beaunity – Empowering Beauty Through Community 

[beaunity.onrender.com](https://beaunity.onrender.com/)  

Beaunity is a forum-like platform where users can create, discover, and participate in challenges, discussions and events — both online and offline. The app brings together beauty enthusiasts, professionals, and brands to share their creativity and knowledge through interactive experiences. Whether you're building a skincare routine, exploring makeup trends, or hosting a beauty workshop, Beaunity helps you grow individually while connecting with a supportive community.

<img width="1660" height="942" alt="image" src="https://github.com/user-attachments/assets/0c41af46-8536-40d8-9c98-db628274be75" />


---

## 💖 The Vision

To empower individuals to embrace their unique selves through collaboration, creativity, and meaningful connections.

---

### Contents
- [Project Setup](docs/project_setup.md)
- [Exploring beaunity](docs/exploring_beaunity.md)
- [App Structure & Api Views](docs/app_structure_and_api_views.md)
- [Role Management](docs/role_management.md)
- [Testing](docs/testing.md)

---

## Core Features

This project is built using a modern Django stack, designed for scalability, performance, and developer productivity. Below are the core components integrated into the application: 

🔐 **User Authentication & JWT Login**
- Secure user registration, login, and logout functionality supporting both JWT-based stateless authentication and traditional login via username, email  or Google Account for web users.

👥 **Join & Follow System**
- Users can create accounts, join the platform, connect and interact with others.

🛠️ **Enhanced Admin Interface with Django Unfold**
- The admin panel is customized using Django Unfold, providing a modern, user-friendly interface with improved layout, theming, and navigation—streamlining content moderation and system management for administrators.

🔗 **Generic Foreign Keys**
- Enable flexible and dynamic model relationships across multiple content types, allowing models to reference any other model seamlessly.

🔍 **Discover by Category**  
- User can browse posts, challenges and events by interests—ranging from skincare and makeup to wellness and self-care.

📝 **Post Creation with Predefined Categories**
- Users can share tips, experiences, or insights by creating posts categorized under predefined topics—encouraging structured interaction and community knowledge sharing.

🧴 **User-Generated Challenges**  
- Users can create challenges with images, meeting links, and categorize them with predefined tags for easy discovery.

🗓️ **Host Online & Offline Events**  
- Organizer host workshops, tutorials, or in-person meetups which user can join.

⭐ Favorites System
- Users can mark challenges, events, and posts as favorites for quick access and personal organization..

💬 **Engage Through Comments & Likes**
- Users can interact with other users by giving feedback, encouragement, and inspiration.

👩‍💼 **Role-Based Permissions**
- Different access levels for admins, moderators, organizers and regular users, including public/private content management. Features include public/private content management, pending post and challenge review pages, dashboard statistics, and group membership switching.

📬 **Approval Workflow**
- Moderators review and approve submitted content such as challenges or posts before they become publicly visible.

🔔 **Automated Reminders & Notifications**
- Scheduled tasks (via Celery & Redis) automatically send email notifications and reminders to keep users engaged. Additionally, email notifications are sent instantly when post or challenge is approved or new account is created.

🌐 **Integrated API Support**
- Select parts of the project expose API endpoints via Django REST Framework, enabling integration with frontend components or external services where needed.

💻 **Responsive UI with Mobile Navigation**
- Responsive design ensures seamless user experience across desktop and mobile devices

🎨 **Tailwind CSS Integration**
- Utilizes Tailwind CSS for rapid UI development, utility-first styling, and consistent design—making customization and responsiveness easier to maintain..
  
📂 **Soft Delete Functionality**
- Instead of permanently deleting profiles users' status is set to 'not active'.

⚙️ **Custom Error Templates (404/403)**
- Friendly and branded error pages improve user experience on forbidden or missing resources.

🧼 **Content Sanitization**
- User-generated HTML content is sanitized using bleach to prevent malicious scripts and ensure safety.


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

--- 

## 🧪 Data for testing

You can test the site live at https://beaunity.onrender.com. Feel free to create a new account or use one of the pre-existing demo accounts:


| Group     | Username   | Password     | Email                   |
|-----------|------------|--------------|-------------------------|
| Superuser | vivi.enn   | Skincare#96  | vivien@example.com      |
| Moderator | alice_sim  | Skincare#92  | alice_sim@example.com   |
| Organizer | bilyanaa   | Glow_Up!18   | b_mladenova@example.com |
| User      | caro_lee99 | Tr3ndySkin*  | degip92859@balincs.com  |
| User      | roxy_foxy  | CmbSkin_L0ve | jomike2985@amirei.com   |



