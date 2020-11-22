from django.urls import path

from .views import CursoList

urlpatterns = [
    path("", CursoList.as_view(), name="cursos_list"),
]
