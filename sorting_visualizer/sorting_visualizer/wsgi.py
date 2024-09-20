"""
WSGI config for sorting_visualizer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

_ = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sorting_visualizer.settings')

application = get_wsgi_application()
