import os # import os module to interact with the operating system
from django.core.wsgi import get_wsgi_application # Importing get_wsgi_application to create a WSGI application object

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_invoice_system.settings') # Setting the default settings module for the Django project

application = get_wsgi_application() # Creating a WSGI application object to serve the Django application
# This WSGI configuration file is used to serve the Django application using a WSGI server.
# It sets the default settings module for the Django project and creates a WSGI application object.