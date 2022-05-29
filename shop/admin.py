from django.contrib import admin
from .models import Book, Category
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Properties in admin panel for Book model
    """
    list_display = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Properties in admin panel for Category model
    """
    list_display = ['name']
