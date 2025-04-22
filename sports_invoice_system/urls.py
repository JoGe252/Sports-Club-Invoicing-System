# This file connects URL paths to app routes.
# It defines the URL structure and includes app-specific URLs.
# It is essential for routing requests to the appropriate views in a Django project.

from django.contrib import admin # Importing the admin module for managing the admin interface
from django.urls import path, include # Importing path and include for URL routing

urlpatterns = [ # List of URL patterns for the project
    path('admin/', admin.site.urls), # Admin interface for managing the application
    # URL pattern for the admin interface, accessible at /admin/
    path('', include('core.urls')),           # Home & dashboard 
    # URL pattern for the core app, accessible at the root URL
    path('accounts/', include('accounts.urls')),  # Login/logout
    # URL pattern for the accounts app, accessible at /accounts/
    # This app handles user authentication and account management
    path('invoices/', include('invoices.urls')),  # Invoice system
]
