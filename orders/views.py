from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
import weasyprint

# Create your views here.


@login_required(login_url='/login')
@csrf_protect
def order_create(request):
    """
    View responsible for rendering /order page and committing order
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            # add coupon to order
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            # add username to order
            order.buyer_username = request.user.username
            order.save()
            # add items from cart to OrderItem object
            for item in cart:
                OrderItem.objects.create(order=order,
                                         book=item['book'],
                                         price=item['price'])

            cart.clear()
            # add order_id to session
            request.session['order_id'] = order.id
            # clear session from coupon_id
            request.session['coupon_id'] = None
            return redirect(reverse('process_payment'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})


@staff_member_required
def admin_order_pdf(request, order_id):
    """
    Renders order pdf based on given order_id
    """
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response)
    return response
