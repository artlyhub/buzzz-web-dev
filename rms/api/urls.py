from django.conf.urls import url

from rms.api.views import (
    WeekSpecsAPIView,
    WeekSpecsDetailAPIView,
    TwoWeekSpecsAPIView,
    TwoWeekSpecsDetailAPIView,
    MonthSpecsAPIView,
    MonthSpecsDetailAPIView,
    QuarterSpecsAPIView,
    QuarterSpecsDetailAPIView,
    HalfYearSpecsAPIView,
    HalfYearSpecsDetailAPIView,
    YearSpecsAPIView,
    YearSpecsDetailAPIView,
)

urlpatterns = [
    url(r'^week/$', WeekSpecsAPIView.as_view(), name='week'),
    url(r'^week/(?P<pk>\d+)/$',
        WeekSpecsAPIView.as_view(), name="week-detail"),

    url(r'^twoweek/$', TwoWeekSpecsAPIView.as_view(), name='twoweek'),
    url(r'^twoweek/(?P<pk>\d+)/$',
        TwoWeekSpecsDetailAPIView.as_view(), name="twoweek-detail"),

    url(r'^month/$', MonthSpecsAPIView.as_view(), name='month'),
    url(r'^month/(?P<pk>\d+)/$',
        MonthSpecsDetailAPIView.as_view(), name="month-detail"),

    url(r'^quarter/$', QuarterSpecsAPIView.as_view(), name='quarter'),
    url(r'^quarter/(?P<pk>\d+)/$',
        QuarterSpecsDetailAPIView.as_view(), name="quarter-detail"),

    url(r'^halfyear/$', HalfYearSpecsAPIView.as_view(), name='halfyear'),
    url(r'^halfyear/(?P<pk>\d+)/$',
        HalfYearSpecsDetailAPIView.as_view(), name="halfyear-detail"),

    url(r'^year/$', YearSpecsAPIView.as_view(), name='year'),
    url(r'^year/(?P<pk>\d+)/$',
        YearSpecsDetailAPIView.as_view(), name="year-detail"),
]
