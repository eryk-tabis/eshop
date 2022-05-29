from django.contrib import admin
from .models import Coupon
# Register your models here.


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """
    Properties in admin panel for Coupons
    """
    list_display = ['code', 'quantity', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['quantity', 'active', 'valid_from', 'valid_to']
    search_fields = ['code']
    