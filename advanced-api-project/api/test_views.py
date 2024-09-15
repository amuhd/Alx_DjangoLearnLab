from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Author, Book

# TEST CREATE BOOK
class BookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book_data = {
            "title": "Harry Potter and the Philosopher's Stone",
            "publication_year": 1997,
            "author": self.author.id
        }
        self.create_url = reverse('book-create')

    def test_create_book(self):
        response = self.client.post(self.create_url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Harry Potter and the Philosopher's Stone")

# TEST GET BOOK
    def test_get_books(self):
        Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        response = self.client.get(reverse('book-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure one book is returned

# TEST UPDATE BOOK
    def test_update_book(self):
        book = Book.objects.create(title="Old Title", publication_year=1995, author=self.author)
        update_data = {"title": "Updated Title", "publication_year": 1995, "author": self.author.id}
        response = self.client.put(reverse('book-update', args=[book.id]), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get().title, "Updated Title")

# TEST DELETE BOOK
    def test_delete_book(self):
        book = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        response = self.client.delete(reverse('book-delete', args=[book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Book should be deleted

# TEST FILTER BOOK
    def test_filter_books(self):
        Book.objects.create(title="Book 1", publication_year=1997, author=self.author)
        Book.objects.create(title="Book 2", publication_year=2000, author=self.author)
        response = self.client.get(f"{reverse('book-list')}?publication_year=1997", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book should match

# TEST SEARCH BOOK
    def test_search_books(self):
        Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author)
        Book.objects.create(title="Fantastic Beasts", publication_year=2001, author=self.author)
        response = self.client.get(f"{reverse('book-list')}?search=Harry", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only 'Harry Potter' should match

# TEST ORDER BOOK
    def test_order_books(self):
        Book.objects.create(title="Book 1", publication_year=1997, author=self.author)
        Book.objects.create(title="Book 2", publication_year=2000, author=self.author)
        response = self.client.get(f"{reverse('book-list')}?ordering=-publication_year", format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Book 2")  # Latest book should come first

# TEST AUTHENTICATION
from django.contrib.auth.models import User

class BookPermissionTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
    
    def test_create_book_authenticated(self):
        author = Author.objects.create(name="George Orwell")
        book_data = {"title": "1984", "publication_year": 1949, "author": author.id}
        response = self.client.post(reverse('book-create'), book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
