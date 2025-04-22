# Defines Role and CustomUser (custom auth model)

from django.db import models # Importing models from django.db to define database models
from django.contrib.auth.models import AbstractUser # Importing AbstractUser to create a custom user model

# Role model (Admin, Member, Coach, Accountant)
class Role(models.Model): # Defining the Role model to represent user roles
    name = models.CharField(max_length=20, unique=True) # Field for role name, must be unique

    def __str__(self): # String representation of the Role model
        return self.name # Returns the name of the role

# Custom user linked to a Role
class CustomUser(AbstractUser): # Defining the CustomUser model to extend the default user model
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True) # Foreign key to the Role model, allows null values

    def __str__(self): # String representation of the CustomUser model
        return f"{self.username} ({self.role.name if self.role else 'No Role'})" # Returns the username and role name (if available) of the user
