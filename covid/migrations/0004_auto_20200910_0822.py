# Generated by Django 3.1.1 on 2020-09-10 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0003_estadisticasporedad'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasosPorEstadoModel',
            fields=[
                ('casos_por_estado_id', models.IntegerField(primary_key=True, serialize=False)),
                ('casos_activos', models.IntegerField(verbose_name='Casos Activos')),
                ('recuperados', models.IntegerField()),
                ('muertes', models.IntegerField()),
                ('casos_por_mil', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CasosPorMunicipioModel',
            fields=[
                ('casos_por_municipio_id', models.IntegerField(primary_key=True, serialize=False)),
                ('casos_activos', models.IntegerField(verbose_name='Casos Activos')),
                ('recuperados', models.IntegerField()),
                ('muertes', models.IntegerField()),
                ('casos_por_cien', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EntidadesModel',
            fields=[
                ('entidad_id', models.IntegerField(primary_key=True, serialize=False)),
                ('clave_entidad', models.IntegerField(verbose_name='Clave de la entidad')),
                ('entidad_federativa', models.CharField(max_length=100, unique=True, verbose_name='Entidad Federativa')),
                ('abreviatura', models.CharField(max_length=6, unique=True)),
                ('poblacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EstadisticasPorEdadModel',
            fields=[
                ('estadisticas_por_edad_id', models.IntegerField(primary_key=True, serialize=False)),
                ('rango', models.CharField(max_length=10, verbose_name='Rango de edad')),
                ('cantidad_casos', models.IntegerField(verbose_name='Cantidad de Casos')),
                ('porcentaje_mortalidad', models.IntegerField(verbose_name='Porcentaje de mortalidad')),
                ('m_diabetes', models.CharField(max_length=10, verbose_name='con Diabetes')),
                ('m_epoc', models.CharField(max_length=10, verbose_name='con EPOC')),
                ('m_asma', models.CharField(max_length=10, verbose_name='con Asma')),
                ('m_hipertension', models.CharField(max_length=10, verbose_name='con Hipertension')),
                ('m_obesidad', models.CharField(max_length=10, verbose_name='con Obesidad')),
                ('m_tabaquismo', models.CharField(max_length=10, verbose_name='con Tabaquismo')),
                ('muertes', models.IntegerField(verbose_name='Muertes')),
                ('recuperados', models.IntegerField(verbose_name='Recuperados')),
                ('sexo', models.CharField(max_length=20, verbose_name='Genero')),
            ],
        ),
        migrations.CreateModel(
            name='MunicipiosModel',
            fields=[
                ('municipio_id', models.IntegerField(primary_key=True, serialize=False)),
                ('clave_municipio', models.IntegerField(verbose_name='Clave de municipio')),
                ('municipio', models.CharField(max_length=100)),
                ('poblacion', models.IntegerField()),
                ('entidad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.entidadesmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='covidModel',
        ),
        migrations.DeleteModel(
            name='EstadisticasPorEdad',
        ),
        migrations.AddField(
            model_name='casospormunicipiomodel',
            name='municipio_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.municipiosmodel'),
        ),
        migrations.AddField(
            model_name='casosporestadomodel',
            name='entidad_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covid.entidadesmodel'),
        ),
    ]