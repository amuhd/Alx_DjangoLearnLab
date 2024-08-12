# delete Book
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