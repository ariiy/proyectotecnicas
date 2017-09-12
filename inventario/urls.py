from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.modelo_inventario, name='modelo_inventario')
]
