from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .portal_publico.views import IndexPortalPublicoView, SobrePortalPublicoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexPortalPublicoView.as_view(), name="index"),
    path("sobre/", SobrePortalPublicoView.as_view(), name="about"),
    path("artigos/", include("gestotus.blog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
