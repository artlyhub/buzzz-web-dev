from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from portfolio.api.serializers import (
    PortfolioSerializer,
    PortfolioHistorySerializer,
)
from portfolio.models import (
    Portfolio,
    PortfolioHistory,
)
from utils.paginations import UserResultPagination, StandardResultPagination

User = get_user_model()


class PortfolioAPIView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination


class PortfolioDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PortfolioHistoryAPIView(generics.ListCreateAPIView):
    queryset = PortfolioHistory.objects.all()
    serializer_class = PortfolioHistorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination


class PortfolioHistoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PortfolioHistory.objects.all()
    serializer_class = PortfolioHistorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
