from decimal import Decimal
from django.conf import settings
from shop.models import Book
from coupons.models import Coupon
class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        # store current applied coupon
        self.coupon_id = self.session.get('coupon_id')
    def add(self, book):
        """
        Add a product to the cart or update its quantity.
        """
        book_id = str(book.id)
        if book_id not in self.cart:
            if book.discount_price is None:
                self.cart[book_id] = {'price': str(book.normal_price)}
            else:
                self.cart[book_id] = {'price': str(book.discount_price)}
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, book):
        """
        Remove a product from the cart.
        """
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        books_ids = self.cart.keys()
        # get the product objects and add them to the cart
        books = Book.objects.filter(id__in=books_ids)
        cart = self.cart.copy()
        for book in books:
            cart[str(book.id)]['book'] = book
        for item in cart.values():
            yield item

    def get_total_price(self):
        # return total price of items in a cart
        return sum(int(item['price']) for item in self.cart.values())

    def clear(self):
        # delete cart session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    @property
    def coupon(self):
        # checking if coupon exists
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)
            except Coupon.DoesNotExist:
                pass
        return None

    def get_discount(self):
        # return a value of a discount
        if self.coupon:
            return self.coupon.discount / Decimal(100) * self.get_total_price()
        return Decimal(0)

    def get_total_price_after_discount(self):
        # return total price of items in a cart after discount is included
        return self.get_total_price() - self.get_discount()

    def __len__(self):
        return len(self.cart)
