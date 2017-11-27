from django.db import models
from django.contrib.postgres.fields import JSONField


class BTC(models.Model):
    date = models.CharField(max_length=8)
    time = models.CharField(max_length=8)
    ask = models.BigIntegerField()
    bid = models.BigIntegerField()

    def __str__(self):
        return '{} {}'.format(self.date, self.time)


class BCH(models.Model):
    date = models.CharField(max_length=8)
    time = models.CharField(max_length=8)
    ask = models.IntegerField()
    bid = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.date, self.time)


class ETH(models.Model):
    date = models.CharField(max_length=8)
    time = models.CharField(max_length=8)
    ask = models.IntegerField()
    bid = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.date, self.time)


class ETC(models.Model):
    date = models.CharField(max_length=8)
    time = models.CharField(max_length=8)
    ask = models.IntegerField()
    bid = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.date, self.time)


class XRP(models.Model):
    date = models.CharField(max_length=8)
    time = models.CharField(max_length=8)
    ask = models.IntegerField()
    bid = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.date, self.time)
