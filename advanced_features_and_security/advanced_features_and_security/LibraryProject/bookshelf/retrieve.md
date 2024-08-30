# retrieve Book
>>> book = Book.objects.get(id=book.id)
>>> book.title, book.author, book.publication_year
('1984', 'George Orwell', 1949)
