Social Media API
A Django-based API for user registration and authentication using Django REST Framework.

Setup
Run Migrations:
python manage.py migrate

Create a Superuser (optional):
python manage.py createsuperuser

Start the Development Server:
python manage.py runserver

Endpoints
Register User
POST /accounts/register/
Request: JSON with username, email, password, bio, and optional profile_picture.
Response: Returns a token or validation error.
Login User
POST /accounts/login/
Request: JSON with username and password.
Response: Returns a token or "Invalid Credentials" error.
User Model Overview
username: Unique identifier.
email: Unique email address.
password: Hashed password.
bio: User biography.
profile_picture: Optional user image.
followers: ManyToMany relationship for following users.