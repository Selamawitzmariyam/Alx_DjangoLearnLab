
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Function-Based View (FBV)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

# Class-Based View (CBV)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# User Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def check_role(role):
    def has_role(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(has_role)

# Admin View
@check_role('Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@check_role('Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@check_role('Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
