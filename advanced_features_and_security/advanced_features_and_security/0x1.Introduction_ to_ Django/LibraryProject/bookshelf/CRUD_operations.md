Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> book = Book.object.create(title="1984", author="George Orwell", publication_year="1949")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Book' has no attribute 'object'. Did you mean: 'objects'?
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year="1949")
>>> book
<Book: 1984>
>>> book = Book.objects.get(id=book.id)
>>> book.title, book.author, book.publication_year
('1984', 'George Orwell', 1949)
>>> book.title = "Nineteen Eighty-Four" 
>>> book.save
<bound method Model.save of <Book: Nineteen Eighty-Four>>
>>> book.title
'Nineteen Eighty-Four'
>>> from bookshelf.models import Book
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
>>> book.title, book.author, book.publication_year
('Nineteen Eighty-Four', 'George Orwell', 1949)
>>> book = Book.objects.get(id=book.id)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\abdul\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\abdul\AppData\Local\Programs\Python\Python312\Lib\site-packages\django\db\models\query.py", line 649, in get
    raise self.model.DoesNotExist(
bookshelf.models.Book.DoesNotExist: Book matching query does not exist.