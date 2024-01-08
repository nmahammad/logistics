from django.db import models

# Create your models here

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

class Customer(models.Model):
    customer_name = models.CharField( null=False)
    customer_email = models.EmailField(null=False)
    customer_address = models.CharField(null=False)
    customer_phone = models.CharField(max_length=20, null=False)

    def serialize(self):
        return {
            'customer_id': self.id,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'customer_address': self.customer_address,
            'customer_phone': self.customer_phone,
        }


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    
    sender_name = models.CharField(max_length=255)
    sender_address = models.CharField(max_length=255)
    sender_email = models.EmailField()
    sender_phone = models.CharField(max_length=20)
    sender_id = models.CharField(max_length=20, null = True)

    # Receiver Information
    receiver_id = models.CharField(max_length=20, null = True)
    receiver_name = models.CharField(max_length=255)
    receiver_address = models.CharField(max_length=255)
    receiver_phone = models.CharField(max_length=20)
    receiver_email =  models.EmailField()


    # Other Order Information
    origin_address = models.CharField(max_length=255, null=False)
    destination_address = models.CharField(max_length=255, null=False)
    order_status = models.CharField(max_length=50, null=True, default='pending' ) 
    order_date = models.DateTimeField(null=True)
    delivery_date = models.DateTimeField(null=True)
    estimated_delivery_date = models.DateTimeField(null=True)
    order_location = models.CharField(max_length=255, null=True)

    def serialize(self):
        return {
            'customer_id': self.customer_id if self.customer_id else None,
            
            'sender_name': self.sender_name,
            'receiver_name': self.receiver_name,
            'origin_address': self.origin_address,
            'destination_address': self.destination_address,
            'order_status': self.order_status,
            'order_date': self.order_date.isoformat(),
            'delivery_date': self.delivery_date.isoformat() if self.delivery_date else None,
            'estimated_delivery_date': self.estimated_delivery_date.isoformat() if self.estimated_delivery_date else None,
            'order_location': self.order_location,
            'customer_name' : self.customer_id__customer_name

        }


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(null=False)
    weight = models.FloatField(null=False)

    def serialize(self):
        return {
            'item_id': self.id,
            'order_id': self.order.id,
            'item_name': self.item_name,
            'quantity': self.quantity,
            'weight': self.weight,
        }

from django.db import models

class Transaction(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50, null=False)
    amount = models.FloatField(null=False)
    transaction_date = models.DateTimeField(null=False)
    payment_method = models.CharField(max_length=50, null=False)
    transaction_status = models.CharField(max_length=50, null=False)

    def serialize(self):
        return {
            'transaction_id': self.id,
            'order_id': self.order_id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'transaction_type': self.transaction_type,
            'amount': self.amount,
            'transaction_date': self.transaction_date.isoformat(),
            'payment_method': self.payment_method,
            'transaction_status': self.transaction_status,
        }

class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=255, null=False)
    warehouse_location = models.CharField(max_length=255, null=False)

    def serialize(self):
        return {
            'warehouse_id': self.id,
            'warehouse_name': self.warehouse_name,
            'warehouse_location': self.warehouse_location,
        }
