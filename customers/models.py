from django.db import models
from django.contrib.auth.models import User

# Model for Customer
class Customer(models.Model):
    # Constants for delete_status
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE, 'LIVE'),
        (DELETE, 'DELETE'),
    )

    # Fields for Customer
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    # Foreign Key to User
    # related_name is used to access the Customer object from User object
    # on_delete=models.CASCADE is used to delete the Customer object when the User object is deleted
    user = models.OneToOneField(User, related_name='customer_profile', on_delete=models.CASCADE)


    # delete_status fields
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

