Authentication Overview:
User Registration: Users can register by providing a username, email, and password.
Login: Users can log in with their credentials.
Logout: Users can log out and be redirected to the home page.
Profile: Authenticated users can view their profile.
Instructions for Testing:
Visit /register/ to register a new user.
After registering, visit /login/ to log in.
Upon logging in, visit /profile/ to view profile details.
Logout by visiting /logout/.
Configuration Details:
blog/urls.py includes routes for login, logout, registration, and profile.
registration/ directory includes templates for authentication (login, register, profile).