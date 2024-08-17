from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

def library_detail(request, library_id):
    library = Library.objects.get(id=library_id)
    return render(request, 'relationship_app/library_detail.html')


from django.views.generic.detail import DetailView
from .models import Library

class BookListView(DetailView):
    model = Book
    template_name = 'relationship_app/list_books.html'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Custom Logout View
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in after reg
            return redirect('home')  # Redirect to a home page or another view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def home(request):
    return render(request, 'relationship_app/home.html')

def profile(request):
    return render(request, 'relationship_app/profile.html')

# Views for users

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from .models import UserProfile

def user_is_admin(user):
    return user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

