# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-15 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('date', models.CharField(max_length=8)),
                ('period', models.CharField(choices=[('Y', 'Yearly'), ('Q', 'Quarterly')], max_length=1)),
                ('sales', models.BigIntegerField(blank=True, null=True)),
                ('profits', models.BigIntegerField(blank=True, null=True)),
                ('term_profit', models.BigIntegerField(blank=True, null=True)),
                ('sales_ret', models.FloatField(blank=True, null=True)),
                ('net_profit_ret', models.FloatField(blank=True, null=True)),
                ('roe', models.FloatField(blank=True, null=True)),
                ('debt_ratio', models.FloatField(blank=True, null=True)),
                ('quick_ratio', models.FloatField(blank=True, null=True)),
                ('reserve_ratio', models.FloatField(blank=True, null=True)),
                ('eps', models.IntegerField(blank=True, null=True)),
                ('bps', models.IntegerField(blank=True, null=True)),
                ('dividend_per_share', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('date', models.CharField(max_length=8)),
                ('size_type', models.CharField(blank=True, choices=[('L', 'Large Cap'), ('M', 'Middle Cap'), ('S', 'Small Cap')], max_length=1, null=True)),
                ('style_type', models.CharField(blank=True, choices=[('G', 'Growth'), ('V', 'Value'), ('D', 'Dividend')], max_length=1, null=True)),
                ('face_val', models.IntegerField(blank=True, null=True)),
                ('stock_nums', models.BigIntegerField(blank=True, null=True)),
                ('market_cap', models.BigIntegerField(blank=True, null=True)),
                ('market_cap_rank', models.IntegerField(blank=True, null=True)),
                ('industry', models.CharField(blank=True, max_length=50, null=True)),
                ('per', models.FloatField(blank=True, null=True)),
                ('pbr', models.FloatField(blank=True, null=True)),
                ('yield_ret', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OHLCV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('date', models.CharField(max_length=8)),
                ('open_price', models.IntegerField()),
                ('high_price', models.IntegerField()),
                ('low_price', models.IntegerField()),
                ('close_price', models.IntegerField()),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('date', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=120)),
                ('market_type', models.CharField(choices=[('KP', 'KOSPI'), ('KD', 'KOSDAQ'), ('ETF', 'Exchange Traded Funds')], max_length=3)),
            ],
        ),
    ]
