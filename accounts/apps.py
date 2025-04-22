# Django's app config (required for migrations to work).
# It is used to configure the app and set its name.
# It is essential for the app to be recognized by Django and to enable features like migrations and admin interface integration.

from django.apps import AppConfig # Importing AppConfig from django.apps to configure the app

class AccountsConfig(AppConfig): # Defining the AccountsConfig class to configure the accounts app
    default_auto_field = 'django.db.models.BigAutoField' # Setting the default auto field type for primary keys
    name = 'accounts' # Setting the name of the app to 'accounts'
