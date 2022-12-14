from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model): 
    title = models.CharField(max_length=50)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateTimeField()
    genres = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

class Collection(models.Model):
    title = models.CharField(max_length=50)

class Library(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=50)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publicationDate = models.DateTimeField(max_length=50)
    ISBN = models.CharField(max_length=50)
    genres = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=50)
    photo = models.FileField()
    collections = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)

class BookInstance(models.Model):
    userId = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bookId = models.ForeignKey(Book, on_delete=models.CASCADE)
    libraryId = models.ForeignKey(Library, on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    borrowedDate = models.DateTimeField()
