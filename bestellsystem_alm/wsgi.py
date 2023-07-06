"""
WSGI config for bestellsystem_alm project
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestellsystem_alm.settings')
application = get_wsgi_application()
