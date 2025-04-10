from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(TestCase):
    """Test cases for the Book API."""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password12345")
        self.client.login(username="testuser", password="password12345")
        # Authenticate user
        self.client.force_authenticate(user=self.user)

        # Create an Author
        self.author = Author.objects.create(name="Joseph joshua")

        # Create a Book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2021,
            author=self.author
        )

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post("/books/create/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_get_books_list(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_single_book(self):
        response = self.client.get(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_update_book(self):
        data = {"title": "Updated Book Title"}
        response = self.client.patch(f"/books/{self.book.id}/update/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book Title")

    def test_delete_book(self):
        response = self.client.delete(f"/books/{self.book.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_unauthorized_access(self):
    def test_unauthorized_access(self):
    self.client.force_authenticate(user=None)  # Remove authentication
    data = {"title": "Unauthorized Book", "publication_year": 2025, "author": self.author.id}
    response = self.client.post("/books/create/", data, format="json")
    # Replace with the expected status code. For example, if unauthenticated access returns 401:
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
