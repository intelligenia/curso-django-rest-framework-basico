# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso', models.CharField(max_length=2, serialize=False, verbose_name='ISO alpha-2', primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nombre oficial (CAPS)')),
                ('local_name', models.CharField(max_length=128, verbose_name='Nombre del pa\xeds')),
                ('iso3', models.CharField(max_length=3, null=True, verbose_name='ISO alpha-3')),
                ('numcode', models.PositiveSmallIntegerField(null=True, verbose_name='ISO num\xe9rico')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Pa\xeds',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('iso', models.CharField(max_length=2, serialize=False, verbose_name='ISO alpha-2', primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nombre oficial')),
                ('numcode', models.PositiveSmallIntegerField(null=True, verbose_name='ISO num\xe9rico')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('iso', models.CharField(max_length=2, serialize=False, verbose_name='ISO alpha-2', primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nombre oficial')),
                ('numcode', models.PositiveSmallIntegerField(null=True, verbose_name='ISO num\xe9rico')),
                ('country', models.ForeignKey(default=b'ES', to='location.Country')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Regi\xf3n',
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
                ('latitude', models.CharField(max_length=64, verbose_name='Latitud')),
                ('longitude', models.CharField(max_length=64, verbose_name='Longitud')),
                ('province', models.ForeignKey(verbose_name='Provincia', to='location.Province')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.AddField(
            model_name='province',
            name='region',
            field=models.ForeignKey(verbose_name='Regi\xf3n', to='location.Region'),
        ),
    ]
