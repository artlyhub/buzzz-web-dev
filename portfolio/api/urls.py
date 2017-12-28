from django.conf.urls import url

from portfolio.api.views import (
    PortfolioAPIView,
    PortfolioDetailAPIView,
    PortfolioDiagnosisAPIView,
    PortfolioOptimizationAPIView,
    PortfolioRatioAPIView,
    PortfolioHistoryAPIView,
    PortfolioHistoryDetailAPIView,
)

portfolio_api_urlpatterns = [
    url(r'^portfolio/$', PortfolioAPIView.as_view(), name="portfolio"),
    url(r'^portfolio/(?P<pk>\d+)/$',
        PortfolioDetailAPIView.as_view(), name="portfolio-detail"),
    url(r'^portfolio/(?P<pk>\d+)/diagnosis/$',
        PortfolioDiagnosisAPIView.as_view(), name="portfolio-diagnosis"),
    url(r'^portfolio/(?P<pk>\d+)/optimization/$',
        PortfolioOptimizationAPIView.as_view(), name="portfolio-optimization"),
    url(r'^portfolio-ratio/$',
        PortfolioRatioAPIView.as_view(), name="portfolio-ratio"),

    url(r'^history/$', PortfolioHistoryAPIView.as_view(), name="history"),
    url(r'^history/(?P<pk>\d+)/$',
        PortfolioHistoryDetailAPIView.as_view(), name="history-detail"),
]
