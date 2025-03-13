from django.db import models

# Model for product
class Product(models.Model):
    # Constants for delete_status
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE, 'LIVE'),
        (DELETE, 'DELETE'),
    )

    # Fields for product
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/')
    
    # priority and delete_status fields
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # String representation of the product
    def __str__(self) -> str:
        return self.title

