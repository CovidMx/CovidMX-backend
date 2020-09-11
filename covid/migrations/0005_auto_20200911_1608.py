# Generated by Django 3.1.1 on 2020-09-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0004_auto_20200910_0822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='casosporestadomodel',
            options={'verbose_name': 'Casos por Estado'},
        ),
        migrations.AlterModelOptions(
            name='casospormunicipiomodel',
            options={'verbose_name': 'Casos por Municipio'},
        ),
        migrations.AlterModelOptions(
            name='entidadesmodel',
            options={'verbose_name': 'Entidad', 'verbose_name_plural': 'Entidades'},
        ),
        migrations.AlterModelOptions(
            name='estadisticasporedadmodel',
            options={'verbose_name': 'Estadistica', 'verbose_name_plural': 'Estadisticas'},
        ),
        migrations.AlterModelOptions(
            name='municipiosmodel',
            options={'verbose_name': 'Municipio', 'verbose_name_plural': 'Municipios'},
        ),
        migrations.AlterField(
            model_name='estadisticasporedadmodel',
            name='m_asma',
            field=models.FloatField(verbose_name='con Asma'),
        ),
        migrations.AlterField(
            model_name='estadisticasporedadmodel',
            name='m_diabetes',
            field=models.FloatField(verbose_name='con Diabetes'),
        ),
        migrations.AlterField(
            model_name='estadisticasporedadmodel',
            name='m_epoc',
            field=models.FloatField(verbose_name='con EPOC'),
        ),
        migrations.AlterField(
            model_name='estadisticasporedadmodel',
            name='m_hipertension',
            field=models.FloatField(verbose_name='con Hipertension'),
        ),
        migrations.AlterField(
            model_name='estadisticasporedadmodel',
            name='m_obesidad',
            field=models.FloatField(max_length=10, verbose_name='con Obesidad'),
        ),
        migrations.AlterField(
            model_name='estadisticasporedadmodel',
            name='m_tabaquismo',
            field=models.FloatField(max_length=10, verbose_name='con Tabaquismo'),
        ),
        migrations.AlterField(
            model_name='estadisticasporedadmodel',
            name='porcentaje_mortalidad',
            field=models.FloatField(verbose_name='Porcentaje de mortalidad'),
        ),
        migrations.AlterModelTable(
            name='casosporestadomodel',
            table='CasosPorEstado',
        ),
        migrations.AlterModelTable(
            name='casospormunicipiomodel',
            table='CasosPorMunicipio',
        ),
        migrations.AlterModelTable(
            name='entidadesmodel',
            table='Entidades',
        ),
        migrations.AlterModelTable(
            name='estadisticasporedadmodel',
            table='EstadisticasPorEdad',
        ),
        migrations.AlterModelTable(
            name='municipiosmodel',
            table='Municipios',
        ),
    ]
