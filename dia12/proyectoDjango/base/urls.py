from django.urls import path

from base import views
from django.contrib.auth.views import LogoutView

app_name = "base"

urlpatterns = [
    path("", views.ListaTareasPendientes.as_view(), name="tareas-pendientes"),
    path("login/", views.Logueo.as_view(), name="login"),
    path("registro", views.Signup.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(next_page="base:login"), name="logout"),
    path("tarea/<int:pk>/", views.DetalleTarea.as_view(), name="tarea-detalle"),
    path(
        "tarea/<int:pk>/eliminar", views.EliminarTarea.as_view(), name="tarea-eliminar"
    ),
    path("tarea/<int:pk>/editar", views.EditarTarea.as_view(), name="tarea-editar"),
    path("tarea/nueva/", views.CrearTarea.as_view(), name="tarea-nueva"),
]
