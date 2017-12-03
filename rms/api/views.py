from rest_framework import generics

from rms.api.serializers import (
    WeekSpecsSerializer,
    TwoWeekSpecsSerializer,
    MonthSpecsSerializer,
    QuarterSpecsSerializer,
    HalfYearSpecsSerializer,
    YearSpecsSerializer,
)
from rms.models import (
    WeekSpecs,
    TwoWeekSpecs,
    MonthSpecs,
    QuarterSpecs,
    HalfYearSpecs,
    YearSpecs,
)
from utils.paginations import UserResultPagination, StandardResultPagination


class WeekSpecsAPIView(generics.ListCreateAPIView):
    queryset = WeekSpecs.objects.all()
    serializer_class = WeekSpecsSerializer
    pagination_class = StandardResultPagination


class WeekSpecsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  WeekSpecs.objects.all()
    serializer_class = WeekSpecsSerializer


class TwoWeekSpecsAPIView(generics.ListCreateAPIView):
    queryset = TwoWeekSpecs.objects.all()
    serializer_class = TwoWeekSpecsSerializer
    pagination_class = StandardResultPagination


class TwoWeekSpecsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  TwoWeekSpecs.objects.all()
    serializer_class = TwoWeekSpecsSerializer


class MonthSpecsAPIView(generics.ListCreateAPIView):
    queryset = MonthSpecs.objects.all()
    serializer_class = MonthSpecsSerializer
    pagination_class = StandardResultPagination


class MonthSpecsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  MonthSpecs.objects.all()
    serializer_class = MonthSpecsSerializer


class QuarterSpecsAPIView(generics.ListCreateAPIView):
    queryset = QuarterSpecs.objects.all()
    serializer_class = QuarterSpecsSerializer
    pagination_class = StandardResultPagination


class QuarterSpecsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  QuarterSpecs.objects.all()
    serializer_class = QuarterSpecsSerializer


class HalfYearSpecsAPIView(generics.ListCreateAPIView):
    queryset = HalfYearSpecs.objects.all()
    serializer_class = HalfYearSpecsSerializer
    pagination_class = StandardResultPagination


class HalfYearSpecsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  HalfYearSpecs.objects.all()
    serializer_class = HalfYearSpecsSerializer


class YearSpecsAPIView(generics.ListCreateAPIView):
    queryset = YearSpecs.objects.all()
    serializer_class = YearSpecsSerializer
    pagination_class = StandardResultPagination


class YearSpecsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  YearSpecs.objects.all()
    serializer_class = YearSpecsSerializer
