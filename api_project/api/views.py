from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer  # Make sure you have a serializer for the Book model

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookList(generics.ListAPIView):
        queryset = Book.objects.all
        serializer_class = BookSerializer
