"""bestellsystem_vereinsfeste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

import accounts.views
import ordering.views
import overview.views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', accounts.views.register, name='register'),
    path('', accounts.views.login_user, name='home'),
    path('bestellung/', ordering.views.order, name='bestellung'),
    path('overview/', overview.views.overview, name='uebersicht'),
    #path('rechnung/', overview.views.drucken, name='rechnung'),
    path('bill/', overview.views.bill, name='bill'),

#TODO wieder rauskommentiert, weil Fehlermeldung auf Handy server() unexpected... documents_root
] #+ static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT) \
  #+ static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
