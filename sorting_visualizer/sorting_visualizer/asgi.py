"""
ASGI config for sorting_visualizer project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

_ = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sorting_visualizer.settings')

application = get_asgi_application()
