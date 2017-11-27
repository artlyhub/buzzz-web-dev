from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^arbiter-api/', include('arbiter.api.urls', namespace='arbiter-api')),
    url(r'^api/', include('restapi.urls', namespace='api')),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^test/$', TemplateView.as_view(template_name='test.html'), name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
