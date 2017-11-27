from django.conf.urls import url

from arbiter.api.views import (
    BTCAPIView,
    BCHAPIView,
    ETHAPIView,
    ETCAPIView,
    XRPAPIView,
)

urlpatterns = [
    url(r'^btc/order/$', BTCAPIView.as_view(), name='btc-order'),
    url(r'^bch/order/$', BCHAPIView.as_view(), name='bch-order'),
    url(r'^eth/order/$', ETHAPIView.as_view(), name='eth-order'),
    url(r'^etc/order/$', ETCAPIView.as_view(), name='etc-order'),
    url(r'^xrp/order/$', XRPAPIView.as_view(), name='xrp-order'),
]
