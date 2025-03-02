from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

class journal(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('bookshelf.CustomUser', on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view journals"),
            ("can_create", "Can create journals"),
            ("can_edit", "Can edit journals"),
            ("can_delete", "Can delete journals"),
        ]

    def __str__(self):
        return self.title