from django.contrib import admin

from .models import Book, Library, Author, Genre

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Genre)
