from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
import datetime
# Create your views here.


# BookListView:
# Handles listing and creation of Book instances. Allows read-only access for unauthenticated users,
# and restricts creation to authenticated users.

# ListView to retrieve all books and filters
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for unauthenticated users
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields to filter by title, author and pub. year
    search_fields = ['title', 'author__name']  # Enable search by title and author's name
    ordering_fields = ['title', 'publication_year']  # Allow ordering by title and year
    ordering = ['title']  # Default ordering by title

# BookDetailView:
# Handles retrieving, updating, and deleting a specific Book instance. Restricts modification (update, delete) to authenticated users.
# Custom validation is performed during update to ensure the publication year is not in the future.

# DetailView to retrieve, update or delete a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated users for update, delete


# Customize CreateView and UpdateView to handle validation in the serializer
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        # Example: Additional behavior or validation during update
        publication_year = serializer.validated_data.get('publication_year')
        if publication_year > datetime.date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

# DeleteView to remove a book by ID
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated users can delete