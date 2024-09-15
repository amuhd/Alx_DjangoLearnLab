from rest_framework import serializers
from .models import Author, Book
import datetime


# BookSerializer handles serialization of all fields in the Book model.
# It includes validation for the publication year to ensure no future dates are allowed.

# Serializer for the Book model, validating that publication_year is not in the future
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to check the publication year
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer handles the serialization of the Author model.
# It includes a nested BookSerializer to display the list of related books for each author.

# Serializer for the Author model, with a nested BookSerializer to show related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
