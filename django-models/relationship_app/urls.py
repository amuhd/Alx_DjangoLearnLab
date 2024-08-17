from django.urls import path
from . import views
from .views import list_books, BookListView, LibraryDetailView
from .views import CustomLoginView, CustomLogoutView, register

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),
]
