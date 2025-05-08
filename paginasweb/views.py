from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Campus, Curso
from django.urls import reverse_lazy


class Inicio(TemplateView):
    template_name = 'paginas/index.html'


class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'


class CampusCreate(CreateView):
    template_name = "paginas/form.html"  # arquivo html com o <form>.
    model = Campus  # classe criada no models.
    fields = ['nome']  # lista com os nomes dos atributos.
    success_url = reverse_lazy('index')  # name da url para redirecionar.
    extra_context = {}


class CursoCreate(CreateView):
    template_name = 'paginasweb/form.html'
    model = Curso
    fields = ['nome', 'campus']
    success_url = reverse_lazy('index')
