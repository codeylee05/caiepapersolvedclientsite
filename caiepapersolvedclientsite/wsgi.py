"""
WSGI config for caiepapersolvedclientsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# my_django_project_wsgi.py

# Add your project directory to the sys.path
project_dir = "/home/Lefa/caiepapersolvedclientsite"
sys.path.append(project_dir)

# Set the environment variable to tell Django where your settings module is located
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'caiepapersolvedclientsite.settings')

# Activate the virtual environment
venv_dir = "/home/Lefa/caiepapersolvedclientsite/venv"
activate_this = os.path.join(venv_dir, "bin", "activate_this.py")
exec(open(activate_this).read(), {"__file__": activate_this})

# Create a WSGI application to serve your Django project
application = get_wsgi_application()
