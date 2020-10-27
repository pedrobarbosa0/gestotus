from django.urls import path

from .views import ArtigosList, ArtigosDetailView

urlpatterns = [
    path("", ArtigosList.as_view(), name="artigos_list"),
    path("<int:pk>", ArtigosDetailView.as_view(), name="artigos_detail"),
]
