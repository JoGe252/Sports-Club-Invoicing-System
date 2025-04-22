from django.contrib import admin # Importing the admin module for managing the admin interface
from .models import Invoice, InvoiceItem, Payment # Importing the Invoice, InvoiceItem, and Payment models for registration in the admin interface

class InvoiceItemInline(admin.TabularInline): # Inline model for displaying invoice items within the invoice admin interface
    model = InvoiceItem # Model to be displayed inline
    extra = 1 # Number of empty forms to display for adding new items

@admin.register(Invoice) # Registering the Invoice model with the admin interface
class InvoiceAdmin(admin.ModelAdmin): # Customizing the admin interface for the Invoice model
    list_display = ['id', 'user', 'status', 'due_date'] # Fields to display in the list view
    inlines = [InvoiceItemInline] # Including the InvoiceItemInline for displaying invoice items within the invoice admin interface

admin.site.register(InvoiceItem) # Registering the InvoiceItem model with the admin interface
admin.site.register(Payment) # Registering the Payment model with the admin interface
# This code registers the Invoice, InvoiceItem, and Payment models with the Django admin interface.
# It allows the admin to manage invoices, invoice items, and payments directly from the admin interface.