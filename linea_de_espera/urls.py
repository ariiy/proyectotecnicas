from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.linea_espera, name='linea_espera')
]
