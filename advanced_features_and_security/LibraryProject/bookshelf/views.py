from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'bookshelf/book_list.html', {'books': books})


from .forms import ExampleForm

def search_view(request):
    form = ExampleForm(request.GET or None)
    if form.is_valid():
        query = form.cleaned_data['query']
        # Perform your search logic here
    return render(request, 'bookshelf/search.html', {'form': form})

from .forms import ExampleForm

def search_view(request):
    form = ExampleForm(request.GET or None)
    return render(request, 'bookshelf/form_example.html', {'form': form})
