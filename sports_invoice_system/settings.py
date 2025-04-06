from pathlib import Path # Importing Path from pathlib for file path handling

BASE_DIR = Path(__file__).resolve().parent.parent # Base directory of the project
# This is the settings file for the Django project "sports_invoice_system".

SECRET_KEY = 'django-insecure-12345' # The secret key for the Django application. This should be kept secret in production.
DEBUG = True # Debug mode. Set to False in production.
ALLOWED_HOSTS = [] # Hosts/domain names that this Django site can serve. Empty list means any host is allowed.
# This should be set to the domain names of thepplication in production.

INSTALLED_APPS = [
    'django.contrib.admin', # Django's admin interface
    'django.contrib.auth', # Django's authentication framework
    'django.contrib.contenttypes', # Django's content types framework
    'django.contrib.sessions', # Django's session framework
    'django.contrib.messages', # Django's messaging framework
    'django.contrib.staticfiles', # Django's static files framework
    'accounts', # Custom app for user accounts and authentication
    'invoices', # Custom app for managing invoices
    'core', # Custom app for core functionalities
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Middleware for security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware', # Middleware for session management
    'django.middleware.common.CommonMiddleware', # Middleware for common functionalities
    'django.middleware.csrf.CsrfViewMiddleware', # Middleware for CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Middleware for authentication
    'django.contrib.messages.middleware.MessageMiddleware', # Middleware for messaging framework
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Middleware for clickjacking protection
]

ROOT_URLCONF = 'sports_invoice_system.urls' # URL configuration for the project
# This file contains the URL patterns for the project.

TEMPLATES = [ # Template settings for rendering HTML templates
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Backend for rendering templates
        'DIRS': [BASE_DIR / "templates"], # Directories to search for templates
        'APP_DIRS': True, # Whether to look for templates in app directories
        'OPTIONS': { # Additional options for template rendering
            'context_processors': [ # Context processors to add variables to the template context
                'django.template.context_processors.debug', # Context processors to add variables to the template context
                'django.template.context_processors.request', # Context processors to add variables to the template context
                'django.contrib.auth.context_processors.auth', # Context processors to add variables to the template context
                'django.contrib.messages.context_processors.messages', # Context processors to add variables to the template context
            ],
        },
    },
]

WSGI_APPLICATION = 'sports_invoice_system.wsgi.application' 
# This file contains the WSGI application for the project.
# wsgi = Web Server Gateway Interface- It’s a Python script that acts as the bridge between your Django app and a web server. 

DATABASES = { # Database settings for the project
    'default': { # Default database configuration
        # SQLite database configuration
        'ENGINE': 'django.db.backends.sqlite3', # Database engine to use
        'NAME': BASE_DIR / 'db.sqlite3', # Path to the database file
    }
}

AUTH_PASSWORD_VALIDATORS = [] # Password validators for the project
# This section can be used to define password complexity requirements.
LANGUAGE_CODE = 'en-us' # Language code for the project
# This setting defines the default language for the project.
TIME_ZONE = 'UTC' # Time zone for the project
# This setting defines the default time zone for the project.
USE_I18N = True # Internationalization settings
# This setting enables internationalization support in the project.
USE_TZ = True # Time zone support
# This setting enables time zone support in the project.
STATIC_URL = 'static/' # URL prefix for static files
# This setting defines the URL prefix for serving static files in the project.

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Default auto field type for models
# This setting defines the default auto field type for models in the project.
AUTH_USER_MODEL = 'accounts.CustomUser' # Custom user model for the project
# This setting defines the custom user model to be used in the project.
