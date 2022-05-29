from eshop.celery import app
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from orders.models import Order


@app.task
def payment_completed(order_id):
    """
    Task to send email with attached invoice in it based on given order_id
    """
    order = Order.objects.get(id=order_id)
    subject = f'My shop - EE Invoice no. {order_id}'
    message = 'Please, find attached the invoice for your recent purchase'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    html = render_to_string('orders/pdf.html', {'order': order})
    out = weasyprint.HTML(string=html).write_pdf()
    email.attach(f'order_{order.id}.pdf', out, 'application/pdf')
    email.send()
