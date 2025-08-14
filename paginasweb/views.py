from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages # Importar messages

from .models import Doador, Instituicao, Status, Doacao, Historia_Inspiradoras

# Views para Páginas Estáticas
class PaginaInicial(TemplateView):
    template_name = 'paginasweb/index.html'

class Sobre(TemplateView):
    template_name = 'paginasweb/sobre.html'

# Views para Criação (Create)
class DoadorCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('listar-doador') # Redirecionar para a lista após o cadastro
    extra_context = {'titulo' : "Cadastrar Doador", "botao" : "Cadastrar"}
    success_message = "Doador cadastrado com sucesso!"

class InstituicaoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('listar-instituicao') # Redirecionar para a lista
    extra_context = {'titulo' : "Cadastrar Instituição", "botao" : "Cadastrar"}
    success_message = "Instituição cadastrada com sucesso!"

class StatusCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('listar-status') # Redirecionar para a lista
    extra_context = {'titulo' : "Cadastrar Status", "botao" : "Cadastrar"}
    success_message = "Status cadastrado com sucesso!"

class DoacaoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('listar-doacao') # Redirecionar para a lista
    extra_context = {'titulo' : "Registrar Doação", "botao" : "Registrar"}
    success_message = "Doação registrada com sucesso!"

class Historia_InspiradorasCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('listar-historia-inspiradora') # Redirecionar para a lista
    extra_context = {'titulo' : "Publicar História Inspiradora", "botao" : "Publicar"}
    success_message = "História Inspiradora publicada com sucesso!"

# Views para Atualização (Update)
class DoadorUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('listar-doador')
    extra_context = {'titulo' : "Editar Doador", "botao" : "Salvar Alterações"}
    success_message = "Doador atualizado com sucesso!"

class InstituicaoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('listar-instituicao')
    extra_context = {'titulo' : "Editar Instituição", "botao" : "Salvar Alterações"}
    success_message = "Instituição atualizada com sucesso!"

class StatusUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('listar-status')
    extra_context = {'titulo' : "Editar Status", "botao" : "Salvar Alterações"}
    success_message = "Status atualizado com sucesso!"

class DoacaoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('listar-doacao')
    extra_context = {'titulo' : "Editar Doação", "botao" : "Salvar Alterações"}
    success_message = "Doação atualizada com sucesso!"

class Historia_InspiradorasUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('listar-historia-inspiradora')
    extra_context = {'titulo' : "Editar História Inspiradora", "botao" : "Salvar Alterações"}
    success_message = "História Inspiradora atualizada com sucesso!"

# Views para Exclusão (Delete)
class DoadorDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doador
    success_url = reverse_lazy('listar-doador')
    extra_context = {'titulo' : "Excluir Doador", "botao" : "Confirmar Exclusão"}
    success_message = "Doador excluído com sucesso!"
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
class InstituicaoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    success_url = reverse_lazy('listar-instituicao')
    extra_context = {'titulo' : "Excluir Instituição", "botao" : "Confirmar Exclusão"}
    success_message = "Instituição excluída com sucesso!"
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class StatusDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Status
    success_url = reverse_lazy('listar-status')
    extra_context = {'titulo' : "Excluir Status", "botao" : "Confirmar Exclusão"}
    success_message = "Status excluído com sucesso!"
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class DoacaoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    success_url = reverse_lazy('listar-doacao')
    extra_context = {'titulo' : "Excluir Doação", "botao" : "Confirmar Exclusão"}
    success_message = "Doação excluída com sucesso!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class Historia_InspiradorasDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('listar-historia-inspiradora')
    extra_context = {'titulo' : "Excluir História Inspiradora", "botao" : "Confirmar Exclusão"}
    success_message = "História Inspiradora excluída com sucesso!"
    
    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

# Views para Listagem (List)
class DoadorList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/doadorList.html'
    model = Doador
    context_object_name = 'doadores' # Nome mais descritivo para o template

class InstituicaoList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/instituicaoList.html'
    model = Instituicao
    context_object_name = 'instituicoes' # Nome mais descritivo para o template

class DoacaoList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/doacaoList.html'
    model = Doacao
    context_object_name = 'doacoes' # Nome mais descritivo para o template

class Historia_InspiradorasList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/historias_inspiradorasList.html'
    model = Historia_Inspiradoras
    context_object_name = 'historias' # Nome mais descritivo para o template

class StatusList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/statusList.html'
    model = Status
    context_object_name = 'status_list' # Nome mais descritivo para o template