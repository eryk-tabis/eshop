from django.contrib import admin
from .models import Order, OrderItem
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.


class OrderItemInLine(admin.TabularInline):
    """
    Properties in admin panel for OrderItem model
    """
    model = OrderItem
    raw_id_fields = ['book']


def order_pdf(obj):
    """
    link to order`s pdf
    """
    url = reverse('admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')


order_pdf.short_description = 'Invoice'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Properties in admin panel for Order model
    """
    list_display = ['id', 'first_name', 'last_name', 'paid', 'created', 'updated', order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInLine]
