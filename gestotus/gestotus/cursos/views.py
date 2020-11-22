from django.views.generic import ListView

from .models import Curso


class CursoList(ListView):
    model = Curso
    paginate_by = 10
    template_name = "cursos/list.html"
    context_object_name = "cursos"
    queryset = Curso.objects.all()
