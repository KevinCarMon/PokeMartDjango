from django.db import models
# Create your models here.

class PokeMart(models.Model):
    nombreObjeto = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    lugar = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    fechaCompra = models.DateField()
