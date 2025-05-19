from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Doador, Instituicao, Status, Doacao, Historia_Inspiradoras


class PaginaInicial(TemplateView):
    template_name = 'paginasweb/index.html'

class Instituicao(TemplateView):
    template_name = 'paginasweb/sobre.html'

class DoadorCreate(CreateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('index')

class InstituicaoCreate(CreateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('index')

class StatusCreate(CreateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('index')

class DoacaoCreate(CreateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('index')

class Historia_InspiradorasCreate(CreateView):
    template_name = 'paginasweb/form.html'
    model = Historia_Inspiradoras
    fields = ['titulo', 'conteudo', 'data_postagem', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('index')


#############################################################################################################

class DoadorUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('index')

class InstituicaoUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('index')

class StatusUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('index')

class DoacaoUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('index')

class Historia_InspiradorasUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Historia_Inspiradoras
    fields = ['titulo', 'conteudo', 'data_postagem', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('index')


################################################################################################################

class DoadorDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doador
    success_url = reverse_lazy('index')

class InstituicaoDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    success_url = reverse_lazy('index')


class DoacaoDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    success_url = reverse_lazy('index')

class Historia_InspiradorasDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Historia_Inspiradoras
    success_url = reverse_lazy('index')

class StatusDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Status
    success_url = reverse_lazy('index')
