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

Adding Comments
Authenticated Users Only: Only logged-in users can add comments to blog posts.
Process: Navigate to a blog post detail page and fill out the comment form, then submit.
Editing Comments
Ownership Required: Users can only edit their own comments.
Process: Click the edit button next to the comment to access the edit form, make changes, and submit.
Deleting Comments
Ownership Required: Only the author of the comment can delete it.
Process: Click the delete button next to the comment to remove it permanently.
Visibility and Permissions
Public Access: All users can view comments on blog posts, regardless of authentication status.
Permission Enforcement: The system checks user authentication and ownership before allowing edits or deletions.

Adding Tags to Posts
When creating or editing a blog post, users can add tags to categorize their content. Here's how it works:

Tag Input Field: In the post creation and editing forms, there is a designated field for tags. Users can enter existing tags or create new ones. Tags should be separated by commas.

Validation: The form validates the input to ensure that tags are unique and correctly formatted.

Saving Tags: Upon submission, the selected tags are associated with the post in the database, enabling efficient organization and retrieval.

Utilizing the Search Bar
Users can easily search for blog content using the search bar available on the site. Here's how:

Search Functionality: The search bar allows users to input keywords related to the post titles, content, or associated tags.

Dynamic Filtering: When a user submits a search query, the application dynamically filters and displays all matching posts based on the entered keywords.

Results Display: The results page shows a list of posts that match the search criteria, providing users with quick access to relevant content.