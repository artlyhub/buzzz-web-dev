from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from restapi.models import (
    Ticker,
    Specs,
    Info,
    OHLCV,
    Financial,
    Specs,
)

User = get_user_model()


class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ('id',
                  'code',
                  'date',
                  'name',
                  'market_type',)


class SpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specs
        fields = ('code',
                  'date',
                  'momentum',
                  'volatility',
                  'correlation',
                  'volume',
                  'momentum_score',
                  'volatility_score',
                  'correlation_score',
                  'volume_score',
                  'total_score',)


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('code',
                  'date',
                  'size_type',
                  'style_type',
                  'face_val',
                  'stock_nums',
                  'market_cap',
                  'market_cap_rank',
                  'industry',
                  'per',
                  'pbr',
                  'yield_ret',)


class OHLCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = OHLCV
        fields = ('code',
                  'date',
                  'open_price',
                  'high_price',
                  'low_price',
                  'close_price',
                  'volume',)


class FinancialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financial
        fields = ('code',
                  'date',
                  'period',
                  'sales',
                  'profits',
                  'term_profit',
                  'sales_ret',
                  'net_profit_ret',
                  'roe',
                  'debt_ratio',
                  'quick_ratio',
                  'reserve_ratio',
                  'eps',
                  'bps',
                  'dividend_per_share',)
