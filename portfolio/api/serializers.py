from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from portfolio.models import Portfolio, PortfolioHistory

User = get_user_model()


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id',
                  'user',
                  'name',
                  'capital',
                  'portfolio_type',
                  'description',
                  'created',
                  'updated',)


class PortfolioHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioHistory
        fields = ('id',
                  'portfolio',
                  'date',
                  'code',
                  'status',
                  'quantity',
                  'price',)
