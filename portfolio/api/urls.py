from django.conf.urls import url

from portfolio.api.views import (
    PortfolioAPIView,
    PortfolioDetailAPIView,
    PortfolioHistoryAPIView,
    PortfolioHistoryDetailAPIView,
)

portfolio_api_urlpatterns = [
    url(r'^portfolio/$', PortfolioAPIView.as_view(), name="portfolio"),
    url(r'^portfolio/(?P<pk>\d+)/$',
        PortfolioDetailAPIView.as_view(), name="portfolio-detail"),

    url(r'^history/$', PortfolioHistoryAPIView.as_view(), name="history"),
    url(r'^history/(?P<pk>\d+)/$',
        PortfolioHistoryDetailAPIView.as_view(), name="history-detail"),
]
