# This script is the entry point for the Django project. It sets up the environment and executes the command line utility for administrative tasks.
# It allows you to run various management commands such as starting the server, creating migrations, and applying them.

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.""" #
import os # import os module to interact with the operating system
import sys # import sys module to access command line arguments

def main(): # define the main function
    """Run administrative tasks.""" # docstring for the main function
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sports_invoice_system.settings') # set the default settings module for the Django project
    try: # try to import Django and execute the command line utility
        from django.core.management import execute_from_command_line # import the execute_from_command_line function from Django's management module
    except ImportError as exc: # if there is an ImportError, catch it
        raise ImportError( # raise a new ImportError with a custom message
            "Couldn't import Django. Make sure it's installed and " # check if Django is installed
            "available on your PYTHONPATH environment variable." # check the PYTHONPATH
        ) from exc # raise the original exception
    execute_from_command_line(sys.argv) # execute the command line utility

if __name__ == '__main__': # check if the script is being run directly
    main() # call the main function
