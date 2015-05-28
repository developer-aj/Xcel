# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll', models.CharField(max_length=60)),
                ('pwd', models.CharField(max_length=60)),
                ('clg', models.CharField(default=b'PUSSGRC', max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='xls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('xfile', models.FileField(upload_to=b'files/%Y/%m/%d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
