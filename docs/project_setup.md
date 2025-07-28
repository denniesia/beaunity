## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.10 or higher** 
- **pip** – Comes with Python, or install via `python -m ensurepip`
- **virtualenv** 
- **Django 5.0+**
- **PostgreSQL 13+**
- **Redis (recommended)**
- **Git** – For cloning the repository
- **Node.js 16+**
- **Celery 5.5**
  
### Step 1: Clone the repository
````python
git clone https://github.com/denniesia/beaunity.git
cd <repository-directory>
````

You need to set up the environment variables to run the project. A .env.template file is included in the repository to guide you.

1. Copy the .env.template file: 
````python
cp .env.template .env
````

2. Edit the .env file and fill in the required values, such as:
   
- SECRET_KEY: A secret key for Django.
- Database connection settings (DB_NAME, DB_USER, DB_PASSWORD, etc.).
- DEBUG: Set to True for development, False for production.
- ALLOWED_HOSTS: Add your allowed hosts, separated by commas.
- ! *The project uses Clodinary, Celery and Google Authentication, so there are keys for these variables as well.* 

  
### Step 2: Create & Activate a Virtual Environment
````python
python -m venv .venv

# Activate

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
````


### Step 3: Install Dependencies
````python
# if needed
pip install --upgrade pip

pip install -r requirements.txt
````

### Step 4: Install Tailwind

This project uses Tailwind. To run the following command you firstly need to have node.js on your machine. 

````python
python manage.py tailwind install

````

### Step 5: Set Up the Database

Ensure PostgreSQL is running and set up your database using the credentials provided in the .env file.

Next, run the following commands to apply database migrations:

````python
python manage.py migrate
````

### Step 6: Create a Superuser

To access the admin panel or Swagger documentation, create a superuser account:

````python
python manage.py createsuperuser
````
Follow the prompts to set up the superuser credentials.


### Step 7: Run the Development Server

Run the server with the following command:

````python
# Start Tailwind watcher (in one terminal)
python manage.py tailwind start

# Run Django server (in another terminal)
python manage.py runserver
````

By default, the server runs on http://127.0.0.1:8000/.

### *(Optional) Step 8: Access API Documentation*

The project contains some API View and uses DRF Spectacular for Swagger documentation.

You can access the API documentation at http://127.0.0.1:8000/api/


---

#### Running Tests
Tests are located in the tests/ directory.

To run the tests:

````python
python manage.py test
````

--- 
Next -> [Exploring Beaunity](https://github.com/denniesia/beaunity/blob/main/docs/exploring_beaunity.md)
--- 
Home -> [Home](https://github.com/denniesia/beaunity/blob/main/README.md)
