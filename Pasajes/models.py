from django.db import models
from Usuarios.models import Usuarios
# Create your models here.
class Pasajes(models.Model):
    user = models.ForeignKey(
        Usuarios,
        null = True,
        on_delete = models.CASCADE,
        verbose_name = "Usuario"
        )
    origin = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        verbose_name = 'Origen'
    )
    destiny = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        verbose_name = 'Destino'
    )
    num_chair = models.IntegerField(
        null = False,
        blank = False,
        verbose_name = 'Numero de Asiento'
    )
    cost = models.FloatField(
        null = False,
        blank = False,
        verbose_name = 'Precio'
    )
    state = models.BooleanField(
        default = True,
        verbose_name = "Cancelado"
    )
    created = models.DateTimeField(
        auto_now_add = "True",
        verbose_name = "Fecha de Creacion"
    )
    updated = models.DateTimeField(
        auto_now = "True",
        verbose_name = "Fecha de Actualizacion"
    )
    class Meta:
        verbose_name = 'Pasaje'
        verbose_name_plural = 'Pasajes'
