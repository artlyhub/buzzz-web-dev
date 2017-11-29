# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-29 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BCH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('time', models.CharField(max_length=8)),
                ('ask', models.IntegerField()),
                ('bid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BTC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('time', models.CharField(max_length=8)),
                ('ask', models.BigIntegerField()),
                ('bid', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ETC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('time', models.CharField(max_length=8)),
                ('ask', models.IntegerField()),
                ('bid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ETH',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('time', models.CharField(max_length=8)),
                ('ask', models.IntegerField()),
                ('bid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='XRP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('time', models.CharField(max_length=8)),
                ('ask', models.IntegerField()),
                ('bid', models.IntegerField()),
            ],
        ),
    ]
