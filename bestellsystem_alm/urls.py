"""
bestellsystem_alm URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),

    path('', include('account.urls')),
    path('overview/', include('overview.urls')),
    path('order/', include('order.urls')),
]