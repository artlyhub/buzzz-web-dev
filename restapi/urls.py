from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns

from restapi.views import (
    TickerAPIView,
    TickerDetailAPIView,
    SpecsAPIView,
    SpecsDetailAPIView,
    TickerUpdatedAPIView,
    InfoAPIView,
    InfoDetailAPIView,
    OHLCVAPIView,
    OHLCVDetailAPIView,
    FinancialAPIView,
    FinancialDetailAPIView,
)

from accounts.api.urls import accounts_api_urlpatterns
from portfolio.api.urls import portfolio_api_urlpatterns

urlpatterns = [
    url(r'^ticker/$', TickerAPIView.as_view(), name='ticker'),
    url(r'^ticker/(?P<pk>\d+)/$', TickerDetailAPIView.as_view(), name='ticker-detail'),
    url(r'^ticker-updated/$', TickerUpdatedAPIView.as_view(), name='ticker-updated'),

    url(r'^specs/$', SpecsAPIView.as_view(), name='specs'),
    url(r'^specs/(?P<pk>\d+)/$', SpecsDetailAPIView.as_view(), name='specs-detail'),

    url(r'^info/$', InfoAPIView.as_view(), name='info'),
    url(r'^info/(?P<pk>\d+)/$', InfoDetailAPIView.as_view(), name='info-detail'),

    url(r'^ohlcv/$', OHLCVAPIView.as_view(), name='ohlcv'),
    url(r'^ohlcv/(?P<pk>\d+)/$', OHLCVDetailAPIView.as_view(), name='ohlcv-detail'),

    url(r'^financial/$', FinancialAPIView.as_view(), name='financial'),
    url(r'^financial/(?P<pk>\d+)/$', FinancialDetailAPIView.as_view(), name='financial-detail'),

    url(r'^rms/', include('rms.api.urls', namespace='rms')),
]

urlpatterns += accounts_api_urlpatterns
urlpatterns += portfolio_api_urlpatterns
urlpatterns = format_suffix_patterns(urlpatterns)
