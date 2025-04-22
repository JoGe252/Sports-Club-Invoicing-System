from django.contrib import admin # Importing the admin module for managing the admin interface
from .models import Role, CustomUser # Importing the Role and CustomUser models for registration in the admin interface
from django.contrib.auth.admin import UserAdmin # Importing UserAdmin to customize the admin interface for the CustomUser model

@admin.register(CustomUser) # Registering the CustomUser model with the admin interface
class CustomUserAdmin(UserAdmin): # Customizing the admin interface for the CustomUser model
    model = CustomUser # Specifying the model for the admin interface
    list_display = ['username', 'email', 'role'] # Fields to display in the list view
    fieldsets = UserAdmin.fieldsets + ( # Adding custom fieldsets to the admin interface
        ('Custom fields', {'fields': ('role',)}), # Adding the role field to the fieldsets
    )

admin.site.register(Role) # Registering the Role model with the admin interface
# This allows the admin to manage user roles directly from the admin interface.
