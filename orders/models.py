from django.db import models
from customers.models import Customer
from products.models import Product

# Model for Order
class Order(models.Model):
    # Constants for delete_status
    LIVE = 1
    DELETE = 0

    DELETE_CHOICES = (
        (LIVE, 'LIVE'),
        (DELETE, 'DELETE'),
    )

    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4

    status_choices = (
        (ORDER_PROCESSED, 'ORDER_PROCESSED'),
        (ORDER_DELIVERED, 'ORDER_DELIVERED'),
        (ORDER_REJECTED, 'ORDER_REJECTED'),
    )

    # Fields for Order
    owner = models.ForeignKey(Customer, related_name='orders', on_delete=models.SET_NULL, null = True)
    
    # order_status fields
    order_status = models.IntegerField(choices=status_choices, default=CART_STAGE)
    
    # delete_status fields
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderedItem(models.Model):

    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, related_name='added_items', on_delete=models.CASCADE)
