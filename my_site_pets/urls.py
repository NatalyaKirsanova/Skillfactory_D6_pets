from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.conf import settings
from django.views.generic.base import TemplateView
from pets.urls import urlpatterns as pets_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += pets_urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)