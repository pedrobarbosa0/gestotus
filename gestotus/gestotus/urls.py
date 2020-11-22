from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .drlicitacao.views import DrLicitacaoListView
from .portal_publico.views import IndexPortalPublicoView, SobrePortalPublicoView
from .cursos.views import

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexPortalPublicoView.as_view(), name="index"),
    path("sobre/", SobrePortalPublicoView.as_view(), name="about"),
    path("drlicitacao/", DrLicitacaoListView.as_view(), name="drlicitacao"),
    path("artigos/", include("gestotus.blog.urls")),
    path("cursos/",)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
