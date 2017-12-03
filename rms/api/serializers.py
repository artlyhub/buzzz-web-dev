from rest_framework import serializers

from rms.models import (
    WeekSpecs,
    TwoWeekSpecs,
    MonthSpecs,
    QuarterSpecs,
    HalfYearSpecs,
    YearSpecs,
)


class WeekSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeekSpecs
        fields = ('id',
                  'code',
                  'date',
                  'momentum',
                  'mom_rank',
                  'volatility',
                  'vol_rank',
                  'correlation',
                  'corr_rank',)


class TwoWeekSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoWeekSpecs
        fields = ('id',
                  'code',
                  'date',
                  'momentum',
                  'mom_rank',
                  'volatility',
                  'vol_rank',
                  'correlation',
                  'corr_rank',)


class MonthSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthSpecs
        fields = ('id',
                  'code',
                  'date',
                  'momentum',
                  'mom_rank',
                  'volatility',
                  'vol_rank',
                  'correlation',
                  'corr_rank',)


class QuarterSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterSpecs
        fields = ('id',
                  'code',
                  'date',
                  'momentum',
                  'mom_rank',
                  'volatility',
                  'vol_rank',
                  'correlation',
                  'corr_rank',)


class HalfYearSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HalfYearSpecs
        fields = ('id',
                  'code',
                  'date',
                  'momentum',
                  'mom_rank',
                  'volatility',
                  'vol_rank',
                  'correlation',
                  'corr_rank',)


class YearSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearSpecs
        fields = ('id',
                  'code',
                  'date',
                  'momentum',
                  'mom_rank',
                  'volatility',
                  'vol_rank',
                  'correlation',
                  'corr_rank',)
