from django.test import TestCase # Importing TestCase from django.test to create test cases
from accounts.models import CustomUser, Role # Importing CustomUser and Role models from accounts app
from invoices.models import Invoice, InvoiceItem # Importing Invoice and InvoiceItem models from invoices app

class InvoiceTests(TestCase): # Defining a test case class for the invoice app tests
    def setUp(self): # Setting up the test case
        role = Role.objects.create(name="Member") # Creating a role instance for the test
        self.user = CustomUser.objects.create_user(username="user1", password="password", role=role) # Creating a user instance for the test
        self.invoice = Invoice.objects.create(user=self.user, due_date="2025-05-01") # Creating an invoice instance for the test
        InvoiceItem.objects.create(invoice=self.invoice, description="Session", quantity=2, unit_price=25.00) # Creating an invoice item instance for the test

    def test_invoice_total_price(self): # Test to check if the total price of the invoice is calculated correctly
        total = sum(item.total_price() for item in self.invoice.items.all()) # Calculating the total price of the invoice
        self.assertEqual(total, 50.00) # Asserting that the total price is equal to 50.00 (2 items at $25.00 each)
