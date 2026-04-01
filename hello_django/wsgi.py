"""
WSGI config for hello_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

# AULA 02 - esgi.py é um servidor para DESENVOLVIMENTO, não é recomendado para produção.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

application = get_wsgi_application()
