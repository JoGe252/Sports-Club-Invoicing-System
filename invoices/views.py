from django.shortcuts import render, get_object_or_404 # Importing render and get_object_or_404 for rendering templates and fetching objects
from django.contrib.auth.decorators import login_required # Importing login_required decorator for protecting views
from django.http import HttpResponse # Importing HttpResponse for sending HTTP responses
from .models import Invoice # Importing the Invoice model for invoice-related operations

# List invoices for user or admin
@login_required # Protect the invoice list view with login_required decorator
def invoice_list(request): # Render the list of invoices for logged-in users
    user = request.user # Get the currently logged-in user
    if user.role.name in ["Admin", "Accountant", "Coach"]: # Check if the user is an admin, accountant, or coach
        invoices = Invoice.objects.all() # If so, fetch all invoices
    else: # Otherwise, fetch only the invoices for the logged-in user
        invoices = Invoice.objects.filter(user=user) # Filter invoices by user
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices}) # Render the invoice list template with the invoices context

# Show invoice detail
@login_required # Protect the invoice detail view with login_required decorator
def invoice_detail(request, pk): # Render the details of a specific invoice
    invoice = get_object_or_404(Invoice, pk=pk) # Fetch the invoice by primary key (pk), or return a 404 error if not found
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice}) # Render the invoice detail template with the invoice context

# Optional: download as "PDF" (fake response for now)
@login_required # Protect the invoice PDF view with login_required decorator
def invoice_pdf(request, pk): # Simulate downloading the invoice as a PDF
    invoice = get_object_or_404(Invoice, pk=pk) # Fetch the invoice by primary key (pk), or return a 404 error if not found
    return HttpResponse(f"Simulated PDF for Invoice #{invoice.id}", content_type='application/pdf') # Return a fake PDF response with invoice ID
