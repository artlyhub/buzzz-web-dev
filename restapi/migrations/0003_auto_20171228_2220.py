# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-28 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specs',
            name='volume',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
