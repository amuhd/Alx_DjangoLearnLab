from django.shortcuts import render

# Create your views here.

from .models import Book

def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'relationship_app/list_books.html', context)

def library_details(request, library_id):
    library = Library.objects.get(id=library_id)
    return render(request, 'relationship_app/library_details.html', {'library': library})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
