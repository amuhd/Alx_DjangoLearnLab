from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import serializers

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = serializers
    permission_classes = [IsAuthenticated]
