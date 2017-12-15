from django.db import models

SIGNAL = (
    ('B', 'Buy'),
    ('S', 'Sell'),
    ('H', 'Hold'),
)

RATING = (
    ('A', 'Strong'),
    ('B', 'Normal'),
    ('C', 'Weak')
)


class KOSPI(models.Model):
    date = models.CharField(max_length=8)
    index = models.FloatField()
    index_change = models.FloatField()
    pct_change = models.FloatField()
    volume = models.BigIntegerField()
    signal = models.CharField(max_length=1,
                              choices=SIGNAL,
                              blank=True,
                              null=True)
    signal_days = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=1,
                              choices=RATING,
                              blank=True,
                              null=True)


class KOSDAQ(models.Model):
    date = models.CharField(max_length=8)
    index = models.FloatField()
    index_change = models.FloatField()
    pct_change = models.FloatField()
    volume = models.BigIntegerField()
    signal = models.CharField(max_length=1,
                              choices=SIGNAL,
                              blank=True,
                              null=True)
    signal_days = models.IntegerField(blank=True, null=True)
    rating = models.CharField(max_length=1,
                              choices=RATING,
                              blank=True,
                              null=True)
