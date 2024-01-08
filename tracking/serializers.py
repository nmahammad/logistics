# serializers.py
from rest_framework import serializers
from .models import User, Customer, Order, OrderItem, Transaction, Warehouse

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'customer_name', 'customer_email', 'customer_address', 'customer_phone']

class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 
            'customer_id',  # You can keep customer_id if needed
            'customer_name',  # Include customer_name
            'receiver_id',
            'origin_address',
            'destination_address',
            'order_status',
            'order_date',
            'delivery_date',
            'estimated_delivery_date',
            'order_location',
            
        ]

    def get_customer_name(self, obj):
        return obj.customer_id.customer_name if obj.customer_id else None


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'order_id', 'item_name', 'quantity', 'weight']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'order_id', 'transaction_type', 'amount', 'transaction_date', 'payment_method', 'transaction_status']

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'warehouse_name', 'warehouse_location']
