from django.db import models
# Create your models here.

class Usuarios(models.Model):
    name = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        verbose_name = 'Nombre de Usuario'
    )
    lastname = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        verbose_name = 'Apellido de Usuario'
    )
    DNI = models.BigIntegerField(
        null = False,
        blank = False,
        verbose_name = "DNI"
    )
    cellphone = models.BigIntegerField(
        null = False,
        blank = False,
        verbose_name = "Numero de Celular"
    )
    address = models.CharField(
        max_length = 100,
        null = False,
        blank = False,
        verbose_name = 'Direccion'
    )
    email = models.EmailField(
        max_length = 200,
        verbose_name = "email"
    ) 
    created = models.DateTimeField(
        auto_now_add = "True",
        verbose_name = "Fecha de Creacion"
    )
    updated = models.DateTimeField(
        auto_now = "True",
        verbose_name = "Fecha de Actualizacion"
    )
    
    def __str__(self):
        return "{0}".format(self.name + ' ' + self.lastname )
        
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
