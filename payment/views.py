from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order, OrderItem
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def payment_process(request):
    """
    View is responsible for rendering /order page
    """
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order_item = OrderItem.objects.all().filter(order=order)
    host = request.get_host()
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        pass
    else:
        # Information necessary for PayPalPaymentsForm
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': f'{total_cost}',
            'item_name': f'Order {order.id}',
            'invoice': str(order.id),
            'currency_code': 'USD',
            'notify_url': f"https://{host}{reverse('paypal-ipn')}",
            'return_url': f"https://{host}{reverse('payment_done')}",
            'cancel_return': f"https://{host}{reverse('payment_cancelled')}",
        }
        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'payment/process.html', {'order': order,
                                                        'form': form,
                                                        'order_item': order_item,
                                                        'total_cost': total_cost})


@csrf_exempt
def return_url(request):
    # returns to profile
    return redirect('profile_view')


@csrf_exempt
def cancel_return(request):
    """
    When payment is canceled, it deletes order from db and returns do main page
    """
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    order.delete()
    return redirect('main_view')
