# This file contains the URL patterns for the project.

from django.contrib import admin # Admin interface for the project
from django.urls import path, include # URL pattern for the project

urlpatterns = [ # URL patterns for the project
    # URL pattern for the admin interface
    path('admin/', admin.site.urls), # Admin interface for managing the project
    path('', include('core.urls')), # URL pattern for the core app
    path('accounts/', include('accounts.urls')), # URL pattern for the accounts app
    path('invoices/', include('invoices.urls')), # URL pattern for the invoices app
]
