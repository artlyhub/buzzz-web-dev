from rest_framework import serializers

from arbiter.models import (
    BTC,
    BCH,
    ETH,
    ETC,
    XRP,
)


class BTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTC
        fields = ('date',
                  'time',
                  'ask',
                  'bid',)


class BCHSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTC
        fields = ('date',
                  'time',
                  'ask',
                  'bid',)


class ETHSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTC
        fields = ('date',
                  'time',
                  'ask',
                  'bid',)


class ETCSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTC
        fields = ('date',
                  'time',
                  'ask',
                  'bid',)


class XRPSerializer(serializers.ModelSerializer):
    class Meta:
        model = BTC
        fields = ('date',
                  'time',
                  'ask',
                  'bid',)
