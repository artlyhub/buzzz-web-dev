from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

MARKET_TYPES = (
    ('KP', 'KOSPI'),
    ('KD', 'KOSDAQ'),
    ('ETF', 'Exchange Traded Funds'),
)

SIZE_TYPES = (
    ('L', 'Large Cap'), # 대형주
    ('M', 'Middle Cap'), # 중형주
    ('S', 'Small Cap'), # 소형주
)

STYLE_TYPES = (
    ('G', 'Growth'), # 성장주
    ('V', 'Value'), # 가치주
    ('D', 'Dividend'), # 배당주
)

PERIOD_TYPES = (
    ('Y', 'Yearly'),
    ('Q', 'Quarterly'),
)


class Ticker(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    name = models.CharField(max_length=120)
    market_type = models.CharField(max_length=3, choices=MARKET_TYPES)

    def __str__(self):
        return '{} {}'.format(self.code, self.name)


# class ETF(models.Model):
#     pass


class Info(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    size_type = models.CharField(max_length=1,
                                 choices=SIZE_TYPES,
                                 blank=True,
                                 null=True) # 사이즈
    style_type = models.CharField(max_length=1,
                                  choices=STYLE_TYPES,
                                  blank=True,
                                  null=True) # 스타일
    face_val = models.IntegerField(blank=True, null=True) # 액면가
    stock_nums = models.BigIntegerField(blank=True, null=True) # 상장주식수
    market_cap = models.BigIntegerField(blank=True, null=True) # 시가총액
    market_cap_rank = models.IntegerField(blank=True, null=True) # 시가총액 순위
    industry = models.CharField(max_length=50,
                                blank=True,
                                null=True) # 산업
    per = models.FloatField(blank=True, null=True) # PER로 성장주/가치주 구분
    pbr = models.FloatField(blank=True, null=True)
    yield_ret = models.FloatField(blank=True, null=True) # 배당수익률

    def __str__(self):
        return self.code


class OHLCV(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=20)
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.code


# class BuySell(models.Model):
#     pass


class Financial(models.Model):
    code = models.CharField(max_length=6)
    date = models.CharField(max_length=8)
    period = models.CharField(max_length=1, choices=PERIOD_TYPES) # 연간, 분기
    sales = models.BigIntegerField(blank=True, null=True) # 매출액
    profits = models.BigIntegerField(blank=True, null=True) # 영업이익
    term_profit = models.BigIntegerField(blank=True, null=True) # 당기순이익
    sales_ret = models.FloatField(blank=True, null=True) # 영업이익률
    net_profit_ret = models.FloatField(blank=True, null=True) # 순이익률
    roe = models.FloatField(blank=True, null=True)
    debt_ratio = models.FloatField(blank=True, null=True) # 부채비율
    quick_ratio = models.FloatField(blank=True, null=True) # 당좌비율
    reserve_ratio = models.FloatField(blank=True, null=True) # 유보율
    eps = models.IntegerField(blank=True, null=True)
    bps = models.IntegerField(blank=True, null=True)
    dividend_per_share = models.IntegerField(blank=True, null=True) # 주당배당금

    def __str__(self):
        return self.code
