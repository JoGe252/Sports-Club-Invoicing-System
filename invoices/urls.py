# Views for listing and viewing invoices
# from django.urls import path # Importing path for URL routing
# from . import views # Importing views from the current directory

from django.urls import path # Importing path for URL routing
from . import views # Importing views from the current directory

urlpatterns = [ # List of URL patterns for the invoices app
    path('', views.invoice_list, name='invoice_list'), # List of invoices
    path('<int:pk>/', views.invoice_detail, name='invoice_detail'), # View invoice details
    path('<int:pk>/download/', views.invoice_pdf, name='invoice_pdf'),  # optional PDF
]
