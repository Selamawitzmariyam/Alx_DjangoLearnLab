from django.conf import settings
from django.conf.urls.static import static
from .views import list_books
from django.urls import path
from .views import book_list, LibraryDetailView  # Import your views

urlpatterns = [
    path('books/', book_list, name='book_list'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
]
