from django.db import models
from django.db import models

class Author(models.Model):
    """
        an author who writes books.

         Fields:
          name: The name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
     Represents a book written by an author.

    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: A ForeignKey linking to the Author model, establishing a one-to-many relationship.
    
    Relationships:
    - Each book is linked to one author (`ForeignKey`).
    - An author can have multiple books (`related_name="books"` allows reverse lookup).
    """
    title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
