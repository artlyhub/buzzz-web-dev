# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restapi', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('capital', models.BigIntegerField(blank=True, null=True)),
                ('portfolio_type', models.CharField(blank=True, choices=[('S', 'Stock'), ('CS', 'Cash + Stock')], max_length=2, null=True)),
                ('description', models.CharField(blank=True, max_length=120, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('status', models.CharField(choices=[('B', 'Bought'), ('S', 'Sold')], max_length=1)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_record', to='restapi.Ticker')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='portfolio.Portfolio')),
            ],
        ),
    ]
