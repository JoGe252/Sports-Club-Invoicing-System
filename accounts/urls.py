# This file contains the URL patterns for the accounts app.

from django.urls import path # URL routing for the application
from django.contrib.auth import views as auth_views # views for authentication

urlpatterns = [ # URL patterns for the accounts app
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), # URL pattern for login view
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'), # URL pattern for logout view
]
