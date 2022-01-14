import imp
from pyexpat import model
from django.contrib import admin
from .models import Author, Book

class BookInlineAdmin(admin.TabularInline):
 model = Book

class AuthorAdmin(admin.ModelAdmin):
 inlines = [BookInlineAdmin]

admin.site.register(Author, AuthorAdmin)
