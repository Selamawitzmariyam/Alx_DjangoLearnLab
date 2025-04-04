import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)", "objects.filter(author=author)
    if author:
        return author.books.all()
    return []

# Query 2: List all books in a specific library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    if library:
        return library.books.all()
    return []

# Query 3: Retrieve the librarian of a specific library
def get_librarian_for_library(library_name):
    library ="Librarian.objects.get(library="
    if library and hasattr(library, 'librarian'):
        return library.librarian
    return None
