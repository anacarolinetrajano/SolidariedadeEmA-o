from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy

from .models import Doador, Instituicao, Status, Doacao, Historia_Inspiradoras

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

class doadorList(LoginRequiredMixin, ListView):
    model = Doador
    template_name = 'doador.html'

class doacaoList(LoginRequiredMixin, ListView):
    model = Doacao
    template_name = 'doacao.html'


class PaginaInicial(TemplateView):
    template_name = 'paginasweb/index.html'

class Sobre(TemplateView):
    template_name = 'paginasweb/sobre.html'

class DoadorCreate(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar doador", "botao" : "Cadastrar"}
    success_message = "Doador criado com sucesso!"

class InstituicaoCreate(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Instituicao", "botao" : "Cadastrar"}
    success_message = "Instituição criada com sucesso!"
class StatusCreate(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Status", "botao" : "Cadastrar"}
    
class DoacaoCreate(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Doacao", "botao" : "Cadastrar"}
    success_message = "Doação criada!"
class Historia_InspiradorasCreate(SuccessMessageMixin,LoginRequiredMixin, CreateView):
    model = Historia_Inspiradoras
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Historia Inspiradoras", "botao" : "Cadastrar"}
    success_message = "Historia Inspiradora criada com sucesso!"

#############################################################################################################

class DoadorUpdate(SuccessMessageMixin,UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Doador", "botao" : "Editar"}
    success_message = "Doador atualizado!"

class InstituicaoUpdate(SuccessMessageMixin,UpdateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Instituicao", "botao" : "Editar"}
    success_message = "Instituição atualizada!"
class StatusUpdate(SuccessMessageMixin,UpdateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Status", "botao" : "Editar"}
    success_message = "Status atualizado!"
class DoacaoUpdate(SuccessMessageMixin,UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Doacao", "botao" : "Editar"}
    success_message = "Doação atualizada!"
class Historia_InspiradorasUpdate(SuccessMessageMixin,UpdateView):
    model = Historia_Inspiradoras
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Cadastrar Historia_Inspiradoras", "botao" : "Editar"}
    success_message = "Historia Inspiradora  atualizada!"

################################################################################################################

class DoadorDelete(SuccessMessageMixin,DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doador
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}
    success_message = "Doador excluido!"
class InstituicaoDelete(SuccessMessageMixin,DeleteView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}
    success_message = "Instituição excluida!"
class StatusDelete(SuccessMessageMixin,DeleteView):
    template_name = 'paginasweb/form.html'
    model = Status
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}
    success_message = "Status excluido!"
class DoacaoDelete(SuccessMessageMixin,DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}
    success_message = "Doação excluida!"
class Historia_InspiradorasDelete(SuccessMessageMixin,DeleteView):
    model = Historia_Inspiradoras
    success_url = reverse_lazy('index')
    extra_context = {'titulo' : "Excluir Instituicao", "botao" : "Excluir"}
    success_message = "Historia Inspiradora excluida!"

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
