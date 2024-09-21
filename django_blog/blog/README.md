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


Blog Post CRUD Operations
This Django blog application supports the following CRUD (Create, Read, Update, Delete) operations for blog posts:

Create: Authenticated users can create new blog posts using the post creation form.
Read: All users, whether authenticated or not, can view the list of blog posts and detailed views of individual posts.
Update: Only the post author can edit their blog posts.
Delete: Only the post author can delete their blog posts.
Permissions with Django Mixins
Permissions for blog posts are enforced using Django’s LoginRequiredMixin and UserPassesTestMixin:

LoginRequiredMixin: Ensures that only authenticated users can create, edit, or delete posts.
UserPassesTestMixin: Restricts access to the update and delete views so that only the author of the post can modify or remove their content.
Navigation Instructions
To view the list of posts, visit the homepage (/).
To create a new post, go to /posts/new/ (only accessible if logged in).
To view a specific post, visit /posts/<post_id>/.
To edit a post, visit /posts/<post_id>/edit/ (only for post authors).
To delete a post, visit /posts/<post_id>/delete/ (only for post authors).