from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    titulo = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        validators=[MinLengthValidator(3), MaxLengthValidator(200)],
        unique=True,
    )
    descripcion = models.TextField(
        null=True,
        blank=True,
        validators=[MinLengthValidator(10), MaxLengthValidator(1000)],
        max_length=1000,
    )
    completado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
