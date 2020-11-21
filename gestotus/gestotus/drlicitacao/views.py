from django.views.generic import ListView

from .models import Link, Categoria


class DrLicitacaoListView(ListView):
    model = Link
    paginate_by = 10
    template_name = "drlicitacao/list.html"
    context_object_name = "links"

    def get_queryset(self):
        queryset = Link.objects.all()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(categoria__nome=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categoria_selecionada"] = self.request.GET.get("q")
        context["categorias"] = Categoria.objects.all()
        return context
