from django.db import models

# Create your models here.

# Each Author can be associated with multiple Books.
# The Author model will represent the author of books
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# It contains information about the title, publication year, and the author
# The Book model will represent the  book and establishes a foreign key relationship with Author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
