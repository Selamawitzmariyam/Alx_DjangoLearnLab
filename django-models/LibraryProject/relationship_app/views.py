from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Book  # Import the Book model
from .models import Library

def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'relationship_app/list_books.html', {'books': books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Ensure this template exists
    context_object_name = "library"
