"""sospet_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from sospet.views import *
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_user, name='login'),
    path('login/submit', login_submit),
    path('', list_all_pets, name='index'),
    path('logout/', logout_user, name='logout'),
    path('pet/all/', list_all_pets, name='list'),
    path('pet/user/', list_user_pets, name='list_user'),
    path('pet/detalhes/<id>/', pet_detalhes, name='detalhes'),
    path('pet/registro/', registro_pet, name='registro_pet'),
    path('pet/registro/submit/', set_pet, name='registrar_pet'),
    path('pet/delete/<id>/', delete_pet, name="delete"),
    path('pet/editar/<id>', editar, name='editar')


] + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)