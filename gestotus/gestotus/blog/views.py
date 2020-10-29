from django.views.generic import ListView, DetailView

from .models import Artigo


class ArtigosList(ListView):
    model = Artigo
    paginate_by = 4
    template_name = "artigos/list.html"
    context_object_name = "artigos"
    queryset = Artigo.objects.all().order_by("data_criacao")


class ArtigosDetailView(DetailView):
    model = Artigo
    context_object_name = "artigo"
    template_name = "artigos/detail.html"
