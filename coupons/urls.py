from django.urls import path
from . import views

app_name = 'coupons'

urlpatterns = [
    path('appply/', views.coupon_apply, name='apply'),
]
