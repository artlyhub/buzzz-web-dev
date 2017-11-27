from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from restapi.serializers import (
    TickerSerializer,
    InfoSerializer,
    OHLCVSerializer,
    FinancialSerializer,
)
from restapi.models import (
    Ticker,
    Info,
    OHLCV,
    Financial,
)
from utils.paginations import UserResultPagination, StandardResultPagination

User = get_user_model()


class TickerAPIView(generics.ListCreateAPIView):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination


class TickerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class InfoAPIView(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination


class InfoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OHLCVAPIView(generics.ListCreateAPIView):
    queryset = OHLCV.objects.all()
    serializer_class = OHLCVSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination


class OHLCVDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OHLCV.objects.all()
    serializer_class = OHLCVSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FinancialAPIView(generics.ListCreateAPIView):
    queryset = Financial.objects.all()
    serializer_class = FinancialSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination


class FinancialDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Financial.objects.all()
    serializer_class = FinancialSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
