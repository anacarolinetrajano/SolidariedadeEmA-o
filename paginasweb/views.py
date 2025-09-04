# FileName: MultipleFiles/views.py
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User, Group

from .models import Doador, Instituicao, Status, Doacao, Historia_Inspiradoras
from .forms import UsuarioCadastroForm


class CadastroUsuarioView(CreateView):
    model = User
    form_class = UsuarioCadastroForm
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo' : "Cadastrar Doador", "botao" : "Cadastrar"}

    def form_valid(self, form):
        url = super().form_valid(form)
        grupo, criado = Group.objects.get_or_create(name='Estudante')
        self.object.groups.add(grupo)
        return url

# Views para Páginas Estáticas
class PaginaInicial(TemplateView):
    template_name = 'paginasweb/index.html'

class Sobre(TemplateView):
    template_name = 'paginasweb/sobre.html'

# Views para Criação (Create) - Modified to save current user
class DoadorCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade'] # 'usuario' is set automatically
    success_url = reverse_lazy('doadorList')
    extra_context = {'titulo' : "Cadastrar Doador", "botao" : "Cadastrar"}
    success_message = "Doador cadastrado com sucesso!"

    def form_valid(self, form):
        form.instance.usuario = self.request.user # Assign the current user
        return super().form_valid(form)

class InstituicaoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('instituicaoList')
    extra_context = {'titulo' : "Cadastrar Instituição", "botao" : "Cadastrar"}
    success_message = "Instituição cadastrada com sucesso!"

    def form_valid(self, form):
        form.instance.usuario = self.request.user # Assign the current user
        return super().form_valid(form)

class StatusCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('statusList')
    extra_context = {'titulo' : "Cadastrar Status", "botao" : "Cadastrar"}
    success_message = "Status cadastrado com sucesso!"
    # If Status also has a 'usuario' field, add form_valid here too:
    # def form_valid(self, form):
    #     form.instance.usuario = self.request.user
    #     return super().form_valid(form)

class DoacaoCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('doacaoList')
    extra_context = {'titulo' : "Registrar Doação", "botao" : "Registrar"}
    success_message = "Doação registrada com sucesso!"

    def form_valid(self, form):
        form.instance.usuario = self.request.user # Assign the current user
        return super().form_valid(form)

class Historia_InspiradorasCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('historias-inspiradorasList')
    extra_context = {'titulo' : "Publicar História Inspiradora", "botao" : "Publicar"}
    success_message = "História Inspiradora publicada com sucesso!"

    def form_valid(self, form):
        form.instance.usuario = self.request.user # Assign the current user
        return super().form_valid(form)

# Views para Atualização (Update) - Modified to filter by current user
class DoadorUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('doadorList')
    extra_context = {'titulo' : "Editar Doador", "botao" : "Salvar Alterações"}
    success_message = "Doador atualizado com sucesso!"

    def get_object(self):
        # Only allow editing of records owned by the current user
        return Doador.objects.get(usuario=self.request.user,pk=self.kwargs["pk"])

class InstituicaoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('instituicaoList')
    extra_context = {'titulo' : "Editar Instituição", "botao" : "Salvar Alterações"}
    success_message = "Instituição atualizada com sucesso!"

    def get_object(self):
        # Only allow editing of records owned by the current user
        return Instituicao.objects.get(usuario=self.request.user,pk=self.kwargs["pk"])

class StatusUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome','pode_editar']
    success_url = reverse_lazy('statusList')
    extra_context = {'titulo' : "Editar Status", "botao" : "Salvar Alterações"}
    success_message = "Status atualizado com sucesso!"
    # If Status also has a 'usuario' field, add get_queryset here too:
    # def get_queryset(self):
    #     return super().get_queryset().filter(usuario=self.request.user)

class DoacaoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('doacaoList')
    extra_context = {'titulo' : "Editar Doação", "botao" : "Salvar Alterações"}
    success_message = "Doação atualizada com sucesso!"

class Historia_InspiradorasUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('historias-inspiradorasList')
    extra_context = {'titulo' : "Editar História Inspiradora", "botao" : "Salvar Alterações"}
    success_message = "História Inspiradora atualizada com sucesso!"

# Views para Exclusão (Delete) - Modified to filter by current user
class DoadorDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doador
    success_url = reverse_lazy('doadorList')
    extra_context = {'titulo' : "Excluir Doador", "botao" : "Confirmar Exclusão"}
    success_message = "Doador excluído com sucesso!"
    
    def get_object(self):
        # Only allow editing of records owned by the current user
        return Doador.objects.get(usuario=self.request.user,pk=self.kwargs["pk"])
    
class InstituicaoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    success_url = reverse_lazy('instituicaoList')
    extra_context = {'titulo' : "Excluir Instituição", "botao" : "Confirmar Exclusão"}
    success_message = "Instituição excluída com sucesso!"
    
    def get_object(self):
        # Only allow editing of records owned by the current user
        return Instituicao.objects.get(usuario=self.request.user,pk=self.kwargs["pk"])

class StatusDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Status
    success_url = reverse_lazy('statusList')
    extra_context = {'titulo' : "Excluir Status", "botao" : "Confirmar Exclusão"}
    success_message = "Status excluído com sucesso!"

    def get_object(self):
        # Only allow editing of records owned by the current user
        return Status.objects.get(usuario=self.request.user,pk=self.kwargs["pk"])
    

class DoacaoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    success_url = reverse_lazy('doacaoList')
    extra_context = {'titulo' : "Excluir Doação", "botao" : "Confirmar Exclusão"}
    success_message = "Doação excluída com sucesso!"
    
    def get_object(self):
        # Only allow editing of records owned by the current user
        return Doacao.objects.get(usuario=self.request.user,pk=self.kwargs["pk"])

class Historia_InspiradorasDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('historias-inspiradorasList')
    extra_context = {'titulo' : "Excluir História Inspiradora", "botao" : "Confirmar Exclusão"}
    success_message = "História Inspiradora excluída com sucesso!"
    
    def get_object(self):
        # Only allow editing of records owned by the current user
        return Historia_Inspiradoras.objects.get(usuario=self.request.user,pk=self.kwargs["pk"])

# Views para Listagem (List) - Modified to filter by current user
class DoadorList(LoginRequiredMixin, ListView):
        template_name = 'paginasweb/doadorList.html'
        model = Doador
        context_object_name = 'doadores'
        
        def get_queryset(self):
            # Lista apenas registros do usuário atual
            return Doador.objects.filter(usuario=self.request.user)

class InstituicaoList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/instituicaoList.html' # Corrected template path
    model = Instituicao
    context_object_name = 'instituicoes'

    def get_queryset(self):
        # Only list records owned by the current user
        return Instituicao.objects.filter(usuario=self.request.user)

class DoacaoList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/doacaoList.html' # Corrected template path
    model = Doacao
    context_object_name = 'doacoes'

    def get_queryset(self):
        # Only list records owned by the current user
        return Doacao.objects.filter(usuario=self.request.user)

class Historia_InspiradorasList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/historias_inspiradorasList.html' # Corrected template path
    model = Historia_Inspiradoras
    context_object_name = 'historias'

    def get_queryset(self):
        # Only list records owned by the current user
        return Historia_Inspiradoras.objects.filter(usuario=self.request.user)

class StatusList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/statusList.html' # Corrected template path
    model = Status
    context_object_name = 'status_list'
    # If Status also has a 'usuario' field, add get_queryset here too:
    # def get_queryset(self):
    #     return self.model.objects.filter(usuario=self.request.user)
