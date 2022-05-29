from django.db import models
# Create your models here.


class Category(models.Model):
    """
    Properties of Category model
    """
    name = models.CharField(
        max_length=50,
        help_text="The name of Category")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Properties of Book model
    """
    title = models.CharField(
        max_length=70,
        help_text="The title of the book")
    description = models.TextField(help_text="The description text")
    description2 = models.TextField(help_text="The second description text")
    publication_date = models.DateTimeField(
        verbose_name="Date the book was published",
        auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    normal_price = models.IntegerField(
        help_text="Normal price for a book",
        blank=False)
    discount_price = models.IntegerField(
        help_text="Discount price for a book",
        blank=True,
        null=True)
    cover = models.ImageField(
        null=True,
        blank=False,
        upload_to="book_covers/")
    program = models.FileField(
        null=True,
        blank=False,
        upload_to="book_content/")
    slug = models.SlugField(max_length=40)
