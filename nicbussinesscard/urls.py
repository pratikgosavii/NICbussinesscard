"""nicbussinesscard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static


from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('add-client', add_client, name='add_client'),
    path('update-client/<random_key_value>', update_client, name='update_client'),
    path('delete-client/<random_key_value>', delete_client, name='delete_client'),
    path('list-client/', list_client, name='list_client'),
    path('showcard/<random_key_value>', show_card, name='show_card'),
    path('', dashboard, name='dashboard'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
