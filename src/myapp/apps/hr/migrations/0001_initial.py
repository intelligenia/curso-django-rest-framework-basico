# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n del objeto')),
                ('last_update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de \xc3\xbaltima actualizaci\xc3\xb3n del objeto')),
                ('first_name', models.CharField(max_length=140)),
                ('last_name', models.CharField(max_length=140)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=140)),
                ('town', models.ForeignKey(related_name='members', default=None, to='location.Town', null=True)),
                ('user', models.OneToOneField(related_name='member', null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
