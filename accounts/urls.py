# Handles login/logout (uses Django built-in views)
# This file defines the URL patterns for the accounts app, which handles user authentication and account management.
# It includes paths for login and logout views, using Django's built-in authentication views.

from django.urls import path # Importing path for defining URL patterns
from django.contrib.auth import views as auth_views # Importing authentication views from Django's auth module

urlpatterns = [ # List of URL patterns for the accounts app
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), # Login view with custom template
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'), # Logout view with redirect to home page after logout
]
