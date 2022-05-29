from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Book
from .cart import Cart
from django.http import HttpResponseRedirect
from coupons.forms import CouponApplyForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def cart_add(request, book_id):
    """
    View is responsible for adding items to a cart, redirects to same item page
    """
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.add(book)
    return redirect('training_programs_item_view', book.slug)


def cart_remove(request, book_id):
    """
    View is responsible for removing items from a cart, redirects to previous page
    """
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login')
def cart_detail(request):
    """
    View is responsible for rendering /cart page
    """
    cart = Cart(request)
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/cart-page.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})
