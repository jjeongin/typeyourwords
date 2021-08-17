"""
WSGI config for project website.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

try:
    if os.environ['PYTHONANYWHERE_DOMAIN']:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings.production'
except KeyError:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings.local')

application = get_wsgi_application()
