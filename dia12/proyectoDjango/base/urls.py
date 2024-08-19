from django.urls import path

from . import views

app_name = "base"

urlpatterns = [
    path("", views.lista_pendientes, name="pendientes"),
]
