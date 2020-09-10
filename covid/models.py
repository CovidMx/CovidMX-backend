from django.db import models

# Create your models here.

class covidModel(models.Model):
    date = models.DateTimeField(verbose_name='Fecha de actualizacion')
    register_id= models.CharField(max_length=10, verbose_name='ID de registro')
    origin = models.IntegerField(verbose_name='Origen')
    sector = models.IntegerField(verbose_name='Sector')
    entity_um = models.IntegerField(verbose_name='Entidad UM')
    gender = models.IntegerField(verbose_name='Sexo')

class EstadisticasPorEdad(models.Model):
    rango = models.IntegerField(verbose_name='Rango')
    cantidad_casos= models.IntegerField(verbose_name='Cantidad de Casos')