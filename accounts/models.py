# Django’s AbstractUser to extend user roles
# This file defines a custom user model for the application.
# It extends the default user model to include additional fields or methods as needed.
# The custom user model is used to manage user roles and permissions in the application.
# The model is defined using Django's ORM, allowing for easy database interactions.
# Importing necessary modules from Django

from django.contrib.auth.models import AbstractUser # Importing AbstractUser to extend the default user model
from django.db import models # Database connection

class CustomUser(AbstractUser):# Custom user model extending AbstractUser
    ROLE_CHOICES = ( # Defining choices for user roles
        ('ADMIN', 'Admin'),#
        ('COACH', 'Coach'),
        ('MEMBER', 'Member'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MEMBER')# Role field with choices

    def __str__(self):# String representation of the user role
        return f"{self.username} ({self.get_role_display()})" # Displaying username and role in string format
# This model can be used to manage user roles in the application.