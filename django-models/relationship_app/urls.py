# relationship_app/urls.py

from django.urls import path
from .views import BookListView, LibraryDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
