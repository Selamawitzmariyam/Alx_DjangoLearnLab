from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

   
    def validate_publication_year(self, value): # Custom validation to prevent future publication years
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
      Serializer for the Author model."
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']