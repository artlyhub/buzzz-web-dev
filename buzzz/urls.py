from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from .views import IndexView, login_view, logout_view

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^arbiter-api/', include('arbiter.api.urls', namespace='arbiter-api')),
    url(r'^api/', include('restapi.urls', namespace='api')),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^test/$', TemplateView.as_view(template_name='test.html'), name='test'),
    url(r'^rms/', include('rms.urls', namespace='rms')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
