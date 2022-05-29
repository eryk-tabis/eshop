from django.db import models
from django.contrib.auth.models import AbstractUser
from shop.models import Book
# Create your models here.


class User(AbstractUser):
    """
    Properties for User model
    """
    username = models.CharField(max_length=20, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    owned_books = models.ManyToManyField(Book, blank=True)
    receive_newsletter = models.BooleanField(default=False, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
