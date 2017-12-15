from django.db import models

from restapi.models import Ticker


class WeekSpecs(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    momentum = models.FloatField(blank=True, null=True)
    mom_rank = models.IntegerField(blank=True, null=True)
    volatility = models.FloatField(blank=True, null=True)
    vol_rank = models.IntegerField(blank=True, null=True)
    correlation = models.FloatField(blank=True, null=True)
    corr_rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.code, self.date)


class TwoWeekSpecs(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    momentum = models.FloatField(blank=True, null=True)
    mom_rank = models.IntegerField(blank=True, null=True)
    volatility = models.FloatField(blank=True, null=True)
    vol_rank = models.IntegerField(blank=True, null=True)
    correlation = models.FloatField(blank=True, null=True)
    corr_rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.code, self.date)


class MonthSpecs(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    momentum = models.FloatField(blank=True, null=True)
    mom_rank = models.IntegerField(blank=True, null=True)
    volatility = models.FloatField(blank=True, null=True)
    vol_rank = models.IntegerField(blank=True, null=True)
    correlation = models.FloatField(blank=True, null=True)
    corr_rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.code, self.date)


class QuarterSpecs(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    momentum = models.FloatField(blank=True, null=True)
    mom_rank = models.IntegerField(blank=True, null=True)
    volatility = models.FloatField(blank=True, null=True)
    vol_rank = models.IntegerField(blank=True, null=True)
    correlation = models.FloatField(blank=True, null=True)
    corr_rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.code, self.date)


class HalfYearSpecs(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    momentum = models.FloatField(blank=True, null=True)
    mom_rank = models.IntegerField(blank=True, null=True)
    volatility = models.FloatField(blank=True, null=True)
    vol_rank = models.IntegerField(blank=True, null=True)
    correlation = models.FloatField(blank=True, null=True)
    corr_rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.code, self.date)


class YearSpecs(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    momentum = models.FloatField(blank=True, null=True)
    mom_rank = models.IntegerField(blank=True, null=True)
    volatility = models.FloatField(blank=True, null=True)
    vol_rank = models.IntegerField(blank=True, null=True)
    correlation = models.FloatField(blank=True, null=True)
    corr_rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.code, self.date)
