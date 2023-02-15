"""proyect_mvt URL Configuration

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
from django.urls import path
from proyect_mvt.views import hola_mundo, vista_template
from family_members.views import create_family_member, list_familiars

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola/", hola_mundo),
    path("vista-template/", vista_template),

    path("create-family-member/", create_family_member),
    path("list-familiars/", list_familiars),
]
