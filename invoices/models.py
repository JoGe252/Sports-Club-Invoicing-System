# Defines Invoice, InvoiceItem, and Payment

from django.db import models # Importing models from django.db to define database models
from django.conf import settings # Importing settings to access project settings

# Invoice assigned to a user
class Invoice(models.Model): # Defining the Invoice model to represent invoices
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Foreign key to the user model, allows cascading delete
    status = models.CharField(max_length=10, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid') # Field for invoice status, default is 'unpaid'
    issued_date = models.DateField(auto_now_add=True) # Field for the date the invoice was issued, automatically set to current date
    due_date = models.DateField() # Field for the due date of the invoice
    created_at = models.DateTimeField(auto_now_add=True) # Field for the date and time the invoice was created, automatically set to current date and time

    def __str__(self): # String representation of the Invoice model
        return f"Invoice #{self.id} for {self.user.username}" # Returns the invoice ID and username of the user associated with the invoice

# Items on the invoice
class InvoiceItem(models.Model): # Defining the InvoiceItem model to represent items on an invoice
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items') # Foreign key to the Invoice model, allows cascading delete
    description = models.TextField() # Field for item description
    quantity = models.PositiveIntegerField() # Field for item quantity, must be positive
    unit_price = models.DecimalField(max_digits=10, decimal_places=2) # Field for item unit price, with a maximum of 10 digits and 2 decimal places

    def total_price(self): # Method to calculate the total price of the item
        return self.quantity * self.unit_price # Returns the total price (quantity * unit price)

    def __str__(self): # String representation of the InvoiceItem model
        return f"{self.quantity} x {self.description} @ {self.unit_price}" # Returns the quantity, description, and unit price of the item

# Payment record (optional)
class Payment(models.Model): # Defining the Payment model to represent payments made for invoices
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE) # One-to-one relationship with the Invoice model, allows cascading delete
    amount = models.DecimalField(max_digits=10, decimal_places=2) # Field for payment amount, with a maximum of 10 digits and 2 decimal places
    method = models.CharField(max_length=20, choices=[ # Field for payment method
        ('card', 'Card'), # Payment by card
        ('cash', 'Cash'), # Payment by cash
        ('bank_transfer', 'Bank Transfer') # Payment by bank transfer
    ])
    paid_at = models.DateTimeField(auto_now_add=True) # Field for the date and time the payment was made, automatically set to current date and time

    def __str__(self): # String representation of the Payment model
        return f"Payment for Invoice #{self.invoice.id} - {self.amount} via {self.method}" # Returns the invoice ID, amount, and payment method
