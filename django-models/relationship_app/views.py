from django.shortcuts import render
from .models import Book 


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_details(request, library_id):
    library = Library.objects.get(id=library_id)
    return render(request, 'relationship_app/library_detail.html', {'library': library})



from django.views.generic import ListView, DetailView
from .models import Library

class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
