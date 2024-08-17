from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book 

def list_books(request):
  template = loader.get_template('list_books.html')
  return HttpResponse(template.render())

def library_detail(request):
  template = loader.get_template('library_detail.html')
  return HttpResponse(template.render())

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request, library_id):
    library = Library.objects.get(id=library_id)
    return render(request, 'relationship_app/library_detail.html', {'library': library})



from django.views.generic.detail import DetailView
from .models import Library

class BookListView(DetailView):
    model = Book
    template_name = 'relationship_app/list_books.html'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
