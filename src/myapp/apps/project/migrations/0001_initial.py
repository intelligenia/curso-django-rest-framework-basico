# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n del objeto')),
                ('last_update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de \xc3\xbaltima actualizaci\xc3\xb3n del objeto')),
                ('comment', models.TextField()),
                ('member', models.ForeignKey(related_name='comments', to='hr.Member')),
            ],
            options={
                'ordering': ('creation_datetime',),
            },
        ),
        migrations.CreateModel(
            name='FlowStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n del objeto')),
                ('last_update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de \xc3\xbaltima actualizaci\xc3\xb3n del objeto')),
                ('name', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=256)),
                ('order', models.PositiveIntegerField(default=1, verbose_name=b'order')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n del objeto')),
                ('last_update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de \xc3\xbaltima actualizaci\xc3\xb3n del objeto')),
                ('name', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=256)),
                ('customer', models.ForeignKey(related_name='projects', to='crm.Customer')),
                ('members', models.ManyToManyField(related_name='projects', to='hr.Member')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n del objeto')),
                ('last_update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de \xc3\xbaltima actualizaci\xc3\xb3n del objeto')),
                ('name', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=256)),
                ('order', models.PositiveIntegerField(default=1, verbose_name=b'order')),
                ('deadline', models.DateField(default=None, null=True)),
                ('flow_step', models.ForeignKey(related_name='tasks', to='project.FlowStep')),
                ('members', models.ManyToManyField(related_name='tasks', to='hr.Member')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='flowstep',
            name='project',
            field=models.ForeignKey(related_name='flow_steps', to='project.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(related_name='comments', to='project.Task'),
        ),
    ]
