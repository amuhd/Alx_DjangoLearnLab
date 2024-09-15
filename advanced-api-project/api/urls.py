from django.urls import path
from .views import BookListView, BookDetailView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List Books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # View Books 
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Add delete endpoint
]