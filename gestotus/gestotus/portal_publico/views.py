from django.shortcuts import render
from django.views.generic.base import View

from ..blog.models import Artigo
from ..cursos.models import Curso
from ..parceiros.models import Parceiro
from ..servicos.models import Area
from ..sobre.models import Membro, QuemSomos


class IndexPortalPublicoView(View):
    http_method_names = ['get']

    def get(self, request):
        cursos = Curso.objects.all().order_by('-id')[:3]
        artigos = Artigo.objects.all().order_by('-id')[:2]
        parceiros = Parceiro.objects.all().order_by('-id')[:3]
        areas = Area.objects.all().order_by('-id')[:2]

        context = {
            "artigos": artigos,
            "cursos": cursos,
            "parceiros": parceiros,
            "areas": areas
        }
        return render(request, "index.html", context)


class SobrePortalPublicoView(View):
    http_method_names = ['get']

    def get(self, request):
        quem_somos = QuemSomos.objects.last()
        membros = Membro.objects.all()

        context = {
            "quem_somos": quem_somos,
            "membros": membros
        }
        return render(request, "about.html", context)
