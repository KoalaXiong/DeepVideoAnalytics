# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0025_auto_20170819_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='tevent',
            name='imported',
            field=models.BooleanField(default=False),
        ),
    ]
