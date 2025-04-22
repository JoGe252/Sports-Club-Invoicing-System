# Homepage and dashboard routing
# This file connects URL paths to app routes.
# It defines the URL structure and includes app-specific URLs.

from django.urls import path # Importing path for defining URL patterns
from . import views # Importing views from the current directory

urlpatterns = [ # List of URL patterns for the core app
    path('', views.home, name='home'), # Home page view
    path('dashboard/', views.dashboard, name='dashboard'), # Dashboard view
]
