from django.contrib import admin
from .models import Book  # Import the Book model

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in the list view
    list_filter = ('publication_year', 'author')  # Add filters to the sidebar
    search_fields = ('title', 'author') 
