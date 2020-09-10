from django.db import models

# Create your models here.


class EstadisticasPorEdadModel(models.Model):
    estadisticas_por_edad_id = models.IntegerField(primary_key=True)
    rango = models.CharField(max_length=10,verbose_name='Rango de edad')
    cantidad_casos= models.IntegerField(verbose_name='Cantidad de Casos')
    porcentaje_mortalidad = models.IntegerField(verbose_name='Porcentaje de mortalidad')
    m_diabetes = models.CharField(max_length=10, verbose_name='con Diabetes')
    m_epoc = models.CharField(max_length=10, verbose_name='con EPOC')
    m_asma = models.CharField(max_length=10, verbose_name='con Asma')
    m_hipertension = models.CharField(max_length=10, verbose_name='con Hipertension')
    m_obesidad = models.CharField(max_length=10, verbose_name='con Obesidad')
    m_tabaquismo = models.CharField(max_length=10, verbose_name='con Tabaquismo')
    muertes = models.IntegerField(verbose_name='Muertes')
    recuperados = models.IntegerField(verbose_name='Recuperados')
    sexo = models.CharField(max_length=20, verbose_name='Genero')

    class Meta:
        verbose_name = 'Estadistica'
        verbose_name_plural= 'Estadisticas'        

    def __str__(self):
        return self.rango

class EntidadesModel(models.Model):
    entidad_id = models.IntegerField(primary_key=True)
    clave_entidad = models.IntegerField(verbose_name='Clave de la entidad')
    entidad_federativa = models.CharField(unique=True, null=False, max_length=100, verbose_name='Entidad Federativa')
    abreviatura = models.CharField(unique=True, null=False, max_length=6)
    poblacion = models.IntegerField()

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural= 'Entidades'        

    def __str__(self):
        return self.entidad_federativa

class CasosPorEstadoModel(models.Model):
    casos_por_estado_id = models.IntegerField(primary_key=True)
    casos_activos = models.IntegerField(verbose_name='Casos Activos')
    recuperados = models.IntegerField()
    muertes = models.IntegerField()
    casos_por_mil = models.IntegerField()
    entidad_id = models.ForeignKey(EntidadesModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Casos por Estado'
              

    def __str__(self):
        return self.casos_por_estado_id

class MunicipiosModel(models.Model):
    municipio_id = models.IntegerField(primary_key=True)
    clave_municipio = models.IntegerField(null=False, verbose_name='Clave de municipio')
    municipio = models.CharField(null=False, max_length=100)
    poblacion = models.IntegerField()
    entidad_id = models.ForeignKey(EntidadesModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural= 'Municipios'        

    def __str__(self):
        return self.municipio

class CasosPorMunicipioModel(models.Model):
    casos_por_municipio_id = models.IntegerField(primary_key=True)
    casos_activos = models.IntegerField(verbose_name='Casos Activos')
    recuperados = models.IntegerField()
    muertes = models.IntegerField()
    casos_por_cien = models.IntegerField()
    municipio_id = models.ForeignKey(MunicipiosModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Casos por Municipio'
              

    def __str__(self):
        return self.casos_por_municipio_id