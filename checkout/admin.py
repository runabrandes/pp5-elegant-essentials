from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                        'delivery_cost',
                        'order_total', 'grand_total',)
    list_display = ('order_number', 'date', 'full_name',)
    search_fields = ['order_number', 'date', 'full_name']
    list_filter = ('order_number', 'date', 'full_name',)
    ordering = ('-date',)
    

