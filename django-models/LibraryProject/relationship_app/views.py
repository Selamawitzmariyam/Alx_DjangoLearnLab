
from django import render
from django.shortcuts import render, redirect


from django.views.generic.detail import DetailView
from django.views.generic import DetailView
from django.shortcuts import render,redirect
from .models import Book  # Import the Book model
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
"""
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return render(request, 'relationship_app/register.html', {'form': form})

    else:
        form = UserCreationForm()
        """
class SignupView(UserCreationForm):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'templates/registrations/signup.html'
def book_list(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'relationship_app/list_books.html', {'books': books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Ensure this template exists
    context_object_name = "library"
