# relationship_app/urls.py

from django.urls import path
from .views import list_books, library_details, BookListView, LibraryDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('library/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),
]
