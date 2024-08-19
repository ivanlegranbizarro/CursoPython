from re import template
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tarea


class ListaTareasPendientes(ListView):
    model = Tarea
    context_object_name = "tareas"


class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = "tarea"
