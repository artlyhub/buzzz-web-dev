from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

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
    queryset = Portfolio.objects.all().order_by('-id')
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StandardResultPagination

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
