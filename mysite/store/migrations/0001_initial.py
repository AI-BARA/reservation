# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('people', models.IntegerField(default=0)),
                ('serial', models.IntegerField(default=0)),
                ('solt_butter', models.IntegerField(default=0)),
                ('curry', models.IntegerField(default=0)),
                ('caramel', models.IntegerField(default=0)),
                ('chocolate', models.IntegerField(default=0)),
                ('enter', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
