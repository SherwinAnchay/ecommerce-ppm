from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    MANAGER = 'manager'
    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (MANAGER, 'Store Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)

    def is_manager(self):
        return self.role == self.MANAGER

