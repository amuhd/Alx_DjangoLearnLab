from django.urls import path
from . import views
from .views import list_books, BookListView, LibraryDetailView
from .views import LoginView, LogoutView, register

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view(template_name='logout.html')),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
]
