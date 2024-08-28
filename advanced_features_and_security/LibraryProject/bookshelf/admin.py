from django.contrib import admin
from .models import Book

# Customizing admin.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Register your models here.
admin.site.register(Book)
