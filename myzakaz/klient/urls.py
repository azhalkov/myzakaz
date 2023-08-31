# klient/urls

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('vxod/', TemplateView.as_view(template_name='klient/form/vxod.html'), name='vxod'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
