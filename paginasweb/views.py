from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy

from .models import Doador, Instituicao, Status, Doacao, Historia_Inspiradoras

from django.contrib.auth.mixins import LoginRequiredMixin


class PaginaInicial(TemplateView):
    template_name = 'paginasweb/index.html'

class Sobre(TemplateView):
    template_name = 'paginasweb/sobre.html'

class DoadorCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar doador", "botao" : "Cadastrar"}

class InstituicaoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Instituicao", "botao" : "Cadastrar"}

class StatusCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Status", "botao" : "Cadastrar"}

class DoacaoCreate(LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Doacao", "botao" : "Cadastrar"}

class Historia_InspiradorasCreate(LoginRequiredMixin, CreateView):
    model = Historia_Inspiradoras
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Historia Inspiradoras", "botao" : "Cadastrar"}


#############################################################################################################

class DoadorUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Doador", "botao" : "Editar"}

class InstituicaoUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Instituicao", "botao" : "Editar"}

class StatusUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Status", "botao" : "Editar"}

class DoacaoUpdate(UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Doacao", "botao" : "Editar"}

class Historia_InspiradorasUpdate(UpdateView):
    model = Historia_Inspiradoras
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Historia_Inspiradoras", "botao" : "Editar"}


################################################################################################################

class DoadorDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doador
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}

class InstituicaoDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}

class StatusDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Status
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}

class DoacaoDelete(DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}

class Historia_InspiradorasDelete(DeleteView):
    model = Historia_Inspiradoras
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}


    ######################################################################################################

class DoadorList(ListView):
    template_name = 'paginasweb/lista/doadorList.html'
    model = Doador

class InstituicaoList(ListView):
    template_name = 'paginasweb/lista/instituicaoLista.html'
    model = Instituicao

class DoacaoList(ListView):
    template_name = 'paginasweb/lista/doacaoList.html'
    model = Doacao

class Historia_InspiradorasList(ListView):
    template_name = 'paginasweb/lista/historia_inspiradorasList.html'
    model = Historia_Inspiradoras

class StatusList(ListView):
    template_name = 'paginasweb/lista/statusList.html'
    model = Status
