from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter, OrderingFilter
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
    serializer_class = TickerSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = Ticker.objects.all().order_by('id')
        date_by = self.request.GET.get('date')
        code_by = self.request.GET.get('code')
        if date_by and code_by:
            queryset_list = queryset.filter(date=date_by).filter(code=code_by)
            return queryset_list
        if date_by and not code_by:
            queryset_list = queryset.filter(date=date_by)
            return queryset_list
        if code_by and not date_by:
            queryset_list = queryset.filter(code=code_by)
            return queryset_list
        return queryset


class TickerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TickerUpdatedAPIView(APIView):
    serializer_class = TickerSerializer

    def get(self, request, *args, **kwargs):
        recent_ticker = Ticker.objects.order_by('-id').first()
        updated_date = recent_ticker.date
        return Response({'updated_date': updated_date}, status=HTTP_200_OK)


class InfoAPIView(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination


class InfoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class OHLCVAPIView(generics.ListCreateAPIView):
    serializer_class = OHLCVSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]

    def get_queryset(self, *args, **kwargs):
        queryset = OHLCV.objects.all().order_by('id')
        date_by = self.request.GET.get('date')
        code_by = self.request.GET.get('code')
        if date_by and code_by:
            queryset_list = queryset.filter(date=date_by).filter(code=code_by)
            return queryset_list
        if date_by and not code_by:
            queryset_list = queryset.filter(date=date_by)
            return queryset_list
        if code_by and not date_by:
            queryset_list = queryset.filter(code=code_by)
            return queryset_list
        return queryset


class OHLCVDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OHLCV.objects.all()
    serializer_class = OHLCVSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FinancialAPIView(generics.ListCreateAPIView):
    queryset = Financial.objects.all()
    serializer_class = FinancialSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination


class FinancialDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Financial.objects.all()
    serializer_class = FinancialSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
