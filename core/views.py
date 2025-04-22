from django.shortcuts import render # Importing render for rendering templates
from django.contrib.auth.decorators import login_required # Importing login_required decorator for protecting views

# Public homepage
def home(request): # Render the homepage
    # This view handles the homepage of the application.
    return render(request, 'core/home.html') # Render the home template

# Role-based dashboard
@login_required # Protect the dashboard view with login_required decorator
# This decorator ensures that only authenticated users can access the dashboard.
def dashboard(request): # Render the dashboard for logged-in users
    return render(request, 'core/dashboard.html', {'user': request.user}) # Render the dashboard template with user context
