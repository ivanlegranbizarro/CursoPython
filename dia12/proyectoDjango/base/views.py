from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Tarea


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
