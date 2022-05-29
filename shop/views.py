from django.shortcuts import render, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.


def main(request):
    """
    View is responsible for rendering main page
    """
    books = Book.objects.order_by('-publication_date')[0:3]
    return render(request, 'shop/main.html', {'books': books})


def training_programs(request):
    """
    View is responsible for rendering /training-programs page
    """
    books = Book.objects.all().order_by('-id')
    return render(request, 'shop/training-programs.html', {'books': books})


def training_programs_item(request, slug):
    """
    View is responsible for rendering item page based on given slug
    """
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'shop/training-programs-item.html', {'book': book})


def about_me(request):
    """
    View is responsible for rendering /about-me pgae
    """
    return render(request, 'shop/about-me.html')


@login_required(login_url='/login')
def profile(request):
    """
    View is responsible for rendering /profile page
    """
    return render(request, 'shop/profile.html')

