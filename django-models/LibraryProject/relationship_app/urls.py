
from django.urls import path
from .views import book_list, LibraryDetailView  # Import your views

urlpatterns = [
    path('books/', book_list, name='book_list'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
]