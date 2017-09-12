"""ProyectoFinalTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# DELGADO LUCAS KIMBERLY
# CHANCAY MORALES ARIANNA
# OCTAVO A
from django.conf.urls import url, include
from django.contrib import admin
from linea_de_espera import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^numerosAleatorios/', include('numeros_aleatorios.urls')),
    url(r'^modeloInventario/',include('modelo_inventario.urls')),
    url(r'^lineaEspera/',include('linea_de_espera.urls')),
    url(r'^$', views.linea_espera, name='principal'),

]
