# OnlineCourseHub

OnlineCourseHub is a project for online education developed using the Django framework. The project includes functionality for managing courses, lessons, users, and payments.

## Installation and Running the Project

To install and run the OnlineCourseHub project, follow these steps:

1. Clone the repository: 
git clone https://github.com/OlyaEf/OnlineCourseHub.git

2. Create and activate a virtual environment: 
python -m venv venv
source venv/bin/activate # On Linux / macOS
venv\Scripts\activate # On Windows

3. Install project dependencies:
pip install -r requirements.txt

4. Apply migrations to create the database:
python manage.py migrate

5. Create a superuser for accessing the admin panel:
python manage.py createsuperuser

6. Start the Django development server:
python manage.py runserver

## Project Structure

OnlineCourseHub/
├── config/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── payment/
│ ├── fixtures/
│ │ └── payments_fixture.json
│ ├── management/
│ │ ├── init.py
│ │ └── commands/
│ │ ├── init.py
│ │ └── load_payments.py
│ ├── migrations/
│ │ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializer.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── school/
│ ├── migrations/
│ │ ├── init.py
│ ├── models/
│ │ ├── init.py
│ ├── serializer/
│ │ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── users/
│ ├── migrations/
│ │ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── seriliazers.py
│ ├── tests.py
│ └── views.py
├── venv/
├── .env
├── .env.example
├── .gitignore
├── constants.py
├── manage.py
├── README.md
└── requirements.txt

The project will be available at `http://127.0.0.1:8000/`.

## Functionality Overview

- **payment** - an app for managing user payments.
- **school** - an app for creating and managing courses and lessons.
- **users** - an app for managing users and authentication.

## Technologies Used

- Django - a web development framework.
- Django REST framework - a framework for creating APIs.
- PostgreSQL - a relational database management system.

## Additional Information

If you have any questions or encounter issues with the project, feel free to reach out to the project's author or seek assistance from the Django community.

**Happy coding!**
