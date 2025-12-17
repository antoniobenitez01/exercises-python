from django.contrib import admin
from HolaMundo.models import Author, Book

#Forma de registrar la tabla Author
admin.site.register(Author)
admin.site.register(Book)
