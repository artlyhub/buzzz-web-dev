from django.conf.urls import url

# from django.views.generic.base import RedirectView

from rms.views import (
    RMSHomeView,
    RMSStartView,
)

urlpatterns = [
    url(r'^$', RMSHomeView.as_view(), name='home'),
    url(r'^start/$', RMSStartView.as_view(), name='start'), 
]
