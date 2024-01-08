from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Order, OrderItem, Transaction, Warehouse

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'customer_address', 'customer_phone']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_id', 'receiver_id' ,'origin_address', 'destination_address', 'order_status', 'order_date', 'delivery_date', 'estimated_delivery_date', 'order_location']
    list_filter = ['order_status', 'order_date', 'delivery_date', 'estimated_delivery_date']
    search_fields = ['origin_address', 'destination_address', 'order_location']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'item_name', 'quantity', 'weight']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'transaction_type', 'amount', 'transaction_date', 'payment_method', 'transaction_status']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'warehouse_name', 'warehouse_location']
1