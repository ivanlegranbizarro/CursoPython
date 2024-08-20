from django.urls import path

from base import views

app_name = "base"

urlpatterns = [
    path("", views.ListaTareasPendientes.as_view(), name="tareas-pendientes"),
    path("login/", views.Logueo.as_view(), name="login"),
    path("tarea/<int:pk>/", views.DetalleTarea.as_view(), name="tarea-detalle"),
    path(
        "tarea/<int:pk>/eliminar", views.EliminarTarea.as_view(), name="tarea-eliminar"
    ),
    path("tarea/<int:pk>/editar", views.EditarTarea.as_view(), name="tarea-editar"),
    path("tarea/nueva/", views.CrearTarea.as_view(), name="tarea-nueva"),
]
