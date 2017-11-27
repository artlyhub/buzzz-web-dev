from rest_framework import generics

from arbiter.api.serializers import (
    BTCSerializer,
    BCHSerializer,
    ETHSerializer,
    ETCSerializer,
    XRPSerializer,
)
from arbiter.models import (
    BTC,
    BCH,
    ETH,
    ETC,
    XRP,
)
from utils.paginations import UserResultPagination, StandardResultPagination


class BTCAPIView(generics.ListCreateAPIView):
    queryset = BTC.objects.get_queryset().order_by('-id')
    serializer_class = BTCSerializer
    pagination_class = StandardResultPagination


class BCHAPIView(generics.ListCreateAPIView):
    queryset = BCH.objects.get_queryset().order_by('-id')
    serializer_class = BCHSerializer
    pagination_class = StandardResultPagination


class ETHAPIView(generics.ListCreateAPIView):
    queryset = ETH.objects.get_queryset().order_by('-id')
    serializer_class = ETHSerializer
    pagination_class = StandardResultPagination


class ETCAPIView(generics.ListCreateAPIView):
    queryset = ETC.objects.get_queryset().order_by('-id')
    serializer_class = ETCSerializer
    pagination_class = StandardResultPagination


class XRPAPIView(generics.ListCreateAPIView):
    queryset = XRP.objects.get_queryset().order_by('-id')
    serializer_class = XRPSerializer
    pagination_class = StandardResultPagination
