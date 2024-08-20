from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Tarea


class Logueo(LoginView):
    template_name = "base/login.html"
    field = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("base:tareas-pendientes")


class ListaTareasPendientes(ListView):
    model = Tarea
    context_object_name = "tareas"


class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = "tarea"


class CrearTarea(CreateView):
    model = Tarea
    fields = "__all__"
    success_url = reverse_lazy("base:tareas-pendientes")


class EditarTarea(UpdateView):
    model = Tarea
    fields = "__all__"
    success_url = reverse_lazy("base:tareas-pendientes")


class EliminarTarea(DeleteView):
    model = Tarea
    success_url = reverse_lazy("base:tareas-pendientes")
