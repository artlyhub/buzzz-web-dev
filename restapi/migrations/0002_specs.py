# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('date', models.CharField(max_length=8)),
                ('momentum', models.FloatField(blank=True, null=True)),
                ('volatility', models.FloatField(blank=True, null=True)),
                ('correlation', models.FloatField(blank=True, null=True)),
                ('volume', models.FloatField(blank=True, null=True)),
                ('momentum_score', models.IntegerField(blank=True, null=True)),
                ('volatility_score', models.IntegerField(blank=True, null=True)),
                ('correlation_score', models.IntegerField(blank=True, null=True)),
                ('volume_score', models.IntegerField(blank=True, null=True)),
                ('total_score', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
