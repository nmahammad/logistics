from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'sender_name',
            'sender_address',
            'sender_email',
            'sender_phone',
            'receiver_name',
            'receiver_address',
            'receiver_email',
            'receiver_phone',
            'origin_address',
            'destination_address',
        ]

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        # Add widget attributes or any other customization as needed
