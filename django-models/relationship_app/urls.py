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
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),
]
