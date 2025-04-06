# This file defines the models for the invoices application.

from django.db import models # Database connection
from django.conf import settings # Importing settings for user model

class Invoice(models.Model): # Invoice model to represent an invoice
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='invoices') # ForeignKey to link to the user model
    issued_date = models.DateField(auto_now_add=True) # Date when the invoice was issued
    due_date = models.DateField() # Due date for the invoice payment
    paid = models.BooleanField(default=False) # Boolean field to indicate if the invoice is paid

    def __str__(self): 
        return f"Invoice #{self.pk} for {self.user.username}" # String representation of the invoice

    def total_amount(self): # Total amount
        return sum(item.total_price() for item in self.items.all()) # Method to calculate the total amount of the invoice

class InvoiceItem(models.Model): # InvoiceItem model to represent items in an invoice
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items') # ForeignKey to link to the invoice model
    description = models.CharField(max_length=255) # Description of the item
    quantity = models.PositiveIntegerField() # Quantity of the item
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) # Unit price of the item

    def total_price(self): # Total price method to calculate the total price of the item
        return self.quantity * self.unit_price 

    def __str__(self): # String representation of the invoice item
        return f"{self.description} ({self.quantity} x {self.unit_price})"
