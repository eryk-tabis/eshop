from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from orders.models import Order, OrderItem
from django.shortcuts import get_object_or_404
from user.models import User
from payment.tasks import payment_completed
from django.dispatch import receiver
from django.conf import settings


@receiver(valid_ipn_received)
def ipn_validation(sender, **kwargs):
    """
    Validate hooks received from Paypal
    """
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        # checking if receiver email from paypal is same as email in settings
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            ipn_obj.flag_info
            return

        order = Order.objects.get(id=int(ipn_obj.invoice))
        # checking if received amount of money is same as in order
        if ipn_obj.mc_gross == order.get_total_cost() and ipn_obj.mc_currency == 'USD':
            # changing status in order object
            order.paid = True
            order.save()
            order_items = OrderItem.objects.all().filter(order_id=order.id)
            user = get_object_or_404(User, username=order.buyer_username)
            # adding ordered items to user account
            user.owned_books.add(*[item['book_id'] for item in order_items.all().values()])
            user.save()
            # sending email with invoice
            payment_completed.delay(order.id)
            return
    else:
        return
