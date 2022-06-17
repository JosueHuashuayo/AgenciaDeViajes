from django.db import models
from Usuarios.models import Usuarios
from Pasajes.models import Pasajes
# Create your models here.
class Boleta (models.Model):
    user = models.ForeignKey(
        Usuarios,
        null = True,
        on_delete = models.CASCADE,
        verbose_name = "Usuario"
    )
    ticket = models.ForeignKey(
        Pasajes,
        null = True,
        on_delete = models.CASCADE,
        verbose_name = "Pasaje"
    ) 
    created = models.DateTimeField(
        auto_now_add = "True",
        verbose_name = "Fecha de Creacion"
    )
    updated = models.DateTimeField(
        auto_now = "True",
        verbose_name = "Fecha de Actualizacion"
    )
