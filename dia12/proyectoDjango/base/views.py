from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Tarea
from django.contrib.auth.mixins import LoginRequiredMixin


class Signup(FormView):
    template_name = "base/registro.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("base:tareas-pendientes")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if "usable_password" in form.fields:
            del form.fields["usable_password"]
        return form

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("base:tareas-pendientes")
        return super().get(*args, **kwargs)


class Logueo(LoginView):
    template_name = "base/login.html"
    field = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("base:tareas-pendientes")


class ListaTareasPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = "tareas"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tareas"] = context["tareas"].filter(usuario=self.request.user)
        context["count"] = context["tareas"].filter(completado=False).count()
        return context


class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = "tarea"


class CrearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ["titulo", "descripcion", "completado"]
    success_url = reverse_lazy("base:tareas-pendientes")

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class EditarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ["titulo", "descripcion", "completado"]
    success_url = reverse_lazy("base:tareas-pendientes")


class EliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    success_url = reverse_lazy("base:tareas-pendientes")
