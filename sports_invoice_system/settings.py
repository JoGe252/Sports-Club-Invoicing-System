# This controls the Django app configuration, including apps, DB, templates.
# It also sets up the WSGI application for deployment.
# It is a crucial part of the Django project structure and is essential for running the application.

from pathlib import Path # Importing Path from pathlib to handle file paths

BASE_DIR = Path(__file__).resolve().parent.parent # Setting the base directory to the parent of the current file's directory

SECRET_KEY = 'your-secret-key' # Replace with your actual secret key for production
 
DEBUG = True # Set to False in production

ALLOWED_HOSTS = [] # List of allowed hosts for the application

INSTALLED_APPS = [ # List of installed applications in the Django project
    'django.contrib.admin', # Admin interface for managing the application
    'django.contrib.auth', # Authentication framework for user management
    'django.contrib.contenttypes', # Content types framework for generic relations
    'django.contrib.sessions', # Session framework for managing user sessions
    'django.contrib.messages', # Messaging framework for sending messages between views
    'django.contrib.staticfiles', # Static files framework for serving static files
    
    'accounts', # Custom app for user accounts and authentication
    'invoices', # Custom app for managing invoices
    'core', # Core app for shared functionality and utilities
]

MIDDLEWARE = [ # List of middleware components that process requests and responses
    'django.middleware.security.SecurityMiddleware', # Security middleware for handling security-related tasks
    'django.contrib.sessions.middleware.SessionMiddleware', # Session middleware for managing user sessions
    'django.middleware.common.CommonMiddleware', # Common middleware for handling common tasks
    'django.middleware.csrf.CsrfViewMiddleware', # CSRF middleware for protecting against cross-site request forgery
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Authentication middleware for handling user authentication
    'django.contrib.messages.middleware.MessageMiddleware', # Messaging middleware for sending messages between views
]

ROOT_URLCONF = 'sports_invoice_system.urls' # URL configuration for the project

TEMPLATES = [ # List of template configurations
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Template backend for rendering templates
        'DIRS': [BASE_DIR / 'templates'],  # Template folder
        # List of directories to search for templates
        'APP_DIRS': True, # Enable loading templates from app directories
        'OPTIONS': { # Additional options for the template engine
            'context_processors': [ # List of context processors to be used
                'django.template.context_processors.request', # Request context processor for accessing request data in templates
                'django.contrib.auth.context_processors.auth', # Authentication context processor for accessing user data in templates
                'django.template.context_processors.debug', # Debug context processor for accessing debug information in templates
                'django.template.context_processors.static', # Static context processor for accessing static files in templates
                'django.template.context_processors.tz', # Time zone context processor for accessing time zone information in templates
                'django.contrib.messages.context_processors.messages', # Messages context processor for accessing messages in templates
            ],
        },
    },
]

WSGI_APPLICATION = 'sports_invoice_system.wsgi.application' # WSGI application for serving the project

DATABASES = { # Database configuration for the project
    'default': { # Default database configuration
        'ENGINE': 'django.db.backends.sqlite3', # Database engine to use (SQLite in this case)
        'NAME': BASE_DIR / 'db.sqlite3', # Path to the database file
    }
}

AUTH_USER_MODEL = 'accounts.CustomUser'  # Custom user

# Redirect users to dashboard after login
LOGIN_REDIRECT_URL = 'dashboard' # URL to redirect users after successful login

STATIC_URL = '/static/' # URL prefix for serving static files
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Default auto field type for primary keys
