"""
WSGI config for django_operational_tags_on_specific_static_files project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_operational_tags_on_specific_static_files.settings')

application = get_wsgi_application()
