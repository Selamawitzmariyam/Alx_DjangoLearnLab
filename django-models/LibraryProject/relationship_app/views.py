from django import render


from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.shortcuts import ,redirect
from .models import Book  # Import the Book model
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('book_list')  # Redirect to book list or another view after registration
    else:
        form = UserCreationForm()
def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'relationship_app/templates/list_books.html', {'books': books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/templates/library_detail.html"  # Ensure this template exists
    context_object_name = "library"
