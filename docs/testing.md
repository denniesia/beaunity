# ⭐ Testing

The project includes unit and integration tests, organized into folders corresponding to the models or components they test.

```tree
tests/
├── accounts/
│   ├── models/
│   ├── __init__.py
├── category/
│   ├── forms/
│   ├── views/
│   ├── __init__.py         
├── posts/
│   ├── models/
│   ├── views/
│   ├── __init__.py        
├── __init__.py
````

To run the test please use the command:
````python
python manage.py test
````
