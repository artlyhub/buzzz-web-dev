# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 15:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL, to_field='username')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=11)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
