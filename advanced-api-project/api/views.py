from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView
from django_filters import rest_framework
from rest_framework.filters import filters.OrderingFilter,filters.SearchFilter
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'author__name']
    permission_classes = [permissions.AllowAny]
    ordering_fields = ['title', 'publication_year']  # Fields that can be used for ordering
    ordering = ['title']
class BookDetailView(generics.RetrieveAPIView):
    """
    This view handles the retrieval of a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny] 
class BookCreateView(generics.CreateAPIView): 
    """
    This view handles the creation of a new book in the system.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create books
   
    def perform_create(self, serializer):
    
        publication_year = self.request.data.get("publication_year")
        if publication_year and int(publication_year) > datetime.now().year:
            return Response({"error": "Publication year cannot be in the future."}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(author=self.request.user)
        filter_backends = [SearchFilter]  # Enable search functionality
        search_fields = ['title', 'author__name'] 
        ordering_fields = ['title', 'publication_year']  # Fields that can be used for ordering
        ordering = ['title']
class BookUpdateView(generics.UpdateAPIView):
    """
    This view handles the updating of an existing book in the system.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update books

    def perform_update(self, serializer):
       
        book = self.get_object()

        
        if book.author != self.request.user:
            return Response({"error": "You do not have permission to edit this book."}, status=status.HTTP_403_FORBIDDEN)

        publication_year = self.request.data.get("publication_year")
        if publication_year and int(publication_year) > datetime.now().year:
            return Response({"error": "Publication year cannot be in the future."}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
class BookDeleteView(generics.DestroyAPIView): 
 """
    This view handles the deletion of a book from the system.

    - DELETE request: Allows authenticated users to delete a book.
    - Only authenticated users can delete books.
 """
queryset = Book.objects.all()
serializer_class = BookSerializer
permission_classes = [permissions.IsAuthenticated]
