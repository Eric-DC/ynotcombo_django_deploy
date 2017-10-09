"""
WSGI config for ycombo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys
sys.path.append(os.path.dirname(os.getcwd()) )
from django.core.wsgi import get_wsgi_application
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #magic for Django Deploy

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ycombo.settings")
application = get_wsgi_application()
