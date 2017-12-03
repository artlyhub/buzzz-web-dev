# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HalfYearSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('momentum', models.FloatField(blank=True, null=True)),
                ('mom_rank', models.IntegerField(blank=True, null=True)),
                ('volatility', models.FloatField(blank=True, null=True)),
                ('vol_rank', models.IntegerField(blank=True, null=True)),
                ('correlation', models.FloatField(blank=True, null=True)),
                ('corr_rank', models.IntegerField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='half_year_specs', to='restapi.Ticker')),
            ],
        ),
        migrations.CreateModel(
            name='MonthSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('momentum', models.FloatField(blank=True, null=True)),
                ('mom_rank', models.IntegerField(blank=True, null=True)),
                ('volatility', models.FloatField(blank=True, null=True)),
                ('vol_rank', models.IntegerField(blank=True, null=True)),
                ('correlation', models.FloatField(blank=True, null=True)),
                ('corr_rank', models.IntegerField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='month_specs', to='restapi.Ticker')),
            ],
        ),
        migrations.CreateModel(
            name='QuarterSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('momentum', models.FloatField(blank=True, null=True)),
                ('mom_rank', models.IntegerField(blank=True, null=True)),
                ('volatility', models.FloatField(blank=True, null=True)),
                ('vol_rank', models.IntegerField(blank=True, null=True)),
                ('correlation', models.FloatField(blank=True, null=True)),
                ('corr_rank', models.IntegerField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quarter_specs', to='restapi.Ticker')),
            ],
        ),
        migrations.CreateModel(
            name='TwoWeekSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('momentum', models.FloatField(blank=True, null=True)),
                ('mom_rank', models.IntegerField(blank=True, null=True)),
                ('volatility', models.FloatField(blank=True, null=True)),
                ('vol_rank', models.IntegerField(blank=True, null=True)),
                ('correlation', models.FloatField(blank=True, null=True)),
                ('corr_rank', models.IntegerField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='two_week_specs', to='restapi.Ticker')),
            ],
        ),
        migrations.CreateModel(
            name='WeekSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('momentum', models.FloatField(blank=True, null=True)),
                ('mom_rank', models.IntegerField(blank=True, null=True)),
                ('volatility', models.FloatField(blank=True, null=True)),
                ('vol_rank', models.IntegerField(blank=True, null=True)),
                ('correlation', models.FloatField(blank=True, null=True)),
                ('corr_rank', models.IntegerField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='week_specs', to='restapi.Ticker')),
            ],
        ),
        migrations.CreateModel(
            name='YearSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8)),
                ('momentum', models.FloatField(blank=True, null=True)),
                ('mom_rank', models.IntegerField(blank=True, null=True)),
                ('volatility', models.FloatField(blank=True, null=True)),
                ('vol_rank', models.IntegerField(blank=True, null=True)),
                ('correlation', models.FloatField(blank=True, null=True)),
                ('corr_rank', models.IntegerField(blank=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='year_specs', to='restapi.Ticker')),
            ],
        ),
    ]