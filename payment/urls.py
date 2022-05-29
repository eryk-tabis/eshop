from django.urls import path, include
from . import views

urlpatterns = [
    path('process-payment/', views.payment_process, name='process_payment'),
    path('process-done/', views.return_url, name='payment_done'),
    path('process-canceled/', views.cancel_return, name='payment_cancelled'),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
