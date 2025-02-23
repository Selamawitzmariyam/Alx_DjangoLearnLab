from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path('books/', views.book_list, name='book_list'),  # Function-based view
    path('library/, views.LibraryDetailView, name='library_detail')
]
