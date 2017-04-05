# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n del objeto')),
                ('last_update_datetime', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de \xc3\xbaltima actualizaci\xc3\xb3n del objeto')),
                ('company_name', models.CharField(max_length=140)),
                ('contact_person', models.CharField(max_length=140)),
                ('contact_phone', models.CharField(max_length=15)),
                ('contact_email', models.EmailField(max_length=140)),
                ('town', models.ForeignKey(related_name='customers', default=None, to='location.Town', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
