"""
ASGI config for bestellsystem_alm project
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestellsystem_alm.settings')
application = get_asgi_application()