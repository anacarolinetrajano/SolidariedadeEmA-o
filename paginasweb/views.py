# FileName: MultipleFiles/views.py
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.db.models import Prefetch

from .models import Doador, Instituicao, Status, Doacao, Historia_Inspiradoras
from .forms import UsuarioCadastroForm, DoadorCadastroForm, InstituicaoCadastroForm


# ========================================
# MIXINS PERSONALIZADOS PARA REUTILIZAÇÃO
# ========================================

class UserFilterMixin:
    """
    Mixin para filtrar querysets baseado no usuário atual.
    Superusuários veem tudo, usuários normais veem apenas seus registros.
    """
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(usuario=self.request.user)


class UserObjectPermissionMixin:
    """
    Mixin para controlar acesso a objetos individuais.
    Superusuários podem acessar tudo, usuários normais apenas seus registros.
    """
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_superuser and obj.usuario != self.request.user:
            raise PermissionDenied("Você não tem permissão para acessar este registro.")
        return obj


class SetUserOnSaveMixin:
    """
    Mixin para atribuir automaticamente o usuário atual ao objeto sendo criado.
    """
    def form_valid(self, form):
        if not form.instance.pk:  # Apenas em criação
            form.instance.usuario = self.request.user
        return super().form_valid(form)


class CadastroUsuarioView(CreateView):
    model = User
    form_class = UsuarioCadastroForm
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('login')
    extra_context = {'titulo' : "Cadastrar Usuário", "botao" : "Cadastrar"}

    def form_valid(self, form):
        url = super().form_valid(form)
        return url


# View para cadastro de Doador
# Cria o usuário e o doador simultaneamente
class CadastroDoadorView(CreateView):
    model = User
    form_class = DoadorCadastroForm
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': "Cadastrar-se como Doador",
        'botao': "Criar Conta de Doador",
        'subtitulo': "Faça parte da nossa comunidade de doadores"
    }

    def form_valid(self, form):
        messages.success(self.request, "Cadastro de doador realizado com sucesso! Faça login para continuar.")
        return super().form_valid(form)


# View para cadastro de Instituição
# Cria o usuário e a instituição simultaneamente
class CadastroInstituicaoView(CreateView):
    model = User
    form_class = InstituicaoCadastroForm
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('login')
    extra_context = {
        'titulo': "Cadastrar Instituição",
        'botao': "Criar Conta de Instituição",
        'subtitulo': "Conecte sua instituição com doadores solidários"
    }

    def form_valid(self, form):
        messages.success(self.request, "Cadastro de instituição realizado com sucesso! Faça login para continuar.")
        return super().form_valid(form)

# ========================================
# VIEWS PARA PÁGINAS ESTÁTICAS
# ========================================

class PaginaInicial(TemplateView):
    template_name = 'paginasweb/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Buscar últimas 3 instituições (otimizado - apenas campos necessários)
        context['ultimas_instituicoes'] = Instituicao.objects.only(
            'id', 'nome', 'tipo', 'descricao', 'cidade', 'telefone'
        ).order_by('-id')[:3]
        
        # Buscar últimas 5 histórias com relacionamentos (otimizado com select_related)
        context['ultimas_historias'] = Historia_Inspiradoras.objects.select_related(
            'doador', 'instituicao'
        ).only(
            'id', 'titulo', 'conteudo', 'autor', 'data_postagem',
            'doador__nome', 'instituicao__nome'
        ).order_by('-data_postagem')[:5]
        
        return context

class Sobre(TemplateView):
    template_name = 'paginasweb/sobre.html'

# ========================================
# VIEWS PÚBLICAS (SEM LOGIN)
# ========================================

class InstituicoesPublicasList(ListView):
    """View pública otimizada para listar instituições com paginação"""
    template_name = 'paginasweb/instituicoes_publicas.html'
    model = Instituicao
    context_object_name = 'instituicoes'
    paginate_by = 9  # 9 cards por página (3x3)
    
    def get_queryset(self):
        # Otimizado: busca apenas campos necessários para exibição
        return Instituicao.objects.only(
            'id', 'nome', 'tipo', 'descricao', 'cidade', 'telefone'
        ).order_by('-id')


class HistoriasPublicasList(ListView):
    """View pública otimizada para listar histórias com relacionamentos"""
    template_name = 'paginasweb/historias_publicas.html'
    model = Historia_Inspiradoras
    context_object_name = 'historias'
    paginate_by = 9  # 9 cards por página (3x3)
    
    def get_queryset(self):
        # Otimizado: select_related para evitar N+1 queries
        return Historia_Inspiradoras.objects.select_related(
            'doador', 'instituicao'
        ).only(
            'id', 'titulo', 'conteudo', 'autor', 'data_postagem',
            'doador__nome', 'instituicao__nome'
        ).order_by('-data_postagem')

# ========================================
# VIEWS DE CRIAÇÃO (CREATE)
# ========================================

class DoadorCreate(SetUserOnSaveMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('doadorList')
    extra_context = {'titulo': "Cadastrar Doador", "botao": "Cadastrar"}
    success_message = "Doador cadastrado com sucesso!"


class InstituicaoCreate(SetUserOnSaveMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('instituicaoList')
    extra_context = {'titulo': "Cadastrar Instituição", "botao": "Cadastrar"}
    success_message = "Instituição cadastrada com sucesso!"


class StatusCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome', 'pode_editar']
    success_url = reverse_lazy('statusList')
    extra_context = {'titulo': "Cadastrar Status", "botao": "Cadastrar"}
    success_message = "Status cadastrado com sucesso!"


class DoacaoCreate(SetUserOnSaveMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('doacaoList')
    extra_context = {'titulo': "Registrar Doação", "botao": "Registrar"}
    success_message = "Doação registrada com sucesso!"
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar apenas doadores do usuário atual (exceto superuser)
        if not self.request.user.is_superuser:
            form.fields['doador'].queryset = Doador.objects.filter(
                usuario=self.request.user
            ).only('id', 'nome')
        else:
            form.fields['doador'].queryset = Doador.objects.only('id', 'nome')
        
        # Otimizar queryset de instituições
        form.fields['instituicao'].queryset = Instituicao.objects.only('id', 'nome')
        form.fields['status'].queryset = Status.objects.only('id', 'nome')
        return form


class Historia_InspiradorasCreate(SetUserOnSaveMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('historias-inspiradorasList')
    extra_context = {'titulo': "Publicar História Inspiradora", "botao": "Publicar"}
    success_message = "História Inspiradora publicada com sucesso!"
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Preencher autor automaticamente
        form.fields['autor'].initial = self.request.user.get_full_name() or self.request.user.username
        
        # Filtrar doadores do usuário (campos opcionais)
        if not self.request.user.is_superuser:
            form.fields['doador'].queryset = Doador.objects.filter(
                usuario=self.request.user
            ).only('id', 'nome')
        else:
            form.fields['doador'].queryset = Doador.objects.only('id', 'nome')
        
        # Otimizar queryset de instituições
        form.fields['instituicao'].queryset = Instituicao.objects.only('id', 'nome')
        return form

# ========================================
# VIEWS DE ATUALIZAÇÃO (UPDATE)
# ========================================

class DoadorUpdate(UserObjectPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('doadorList')
    extra_context = {'titulo': "Editar Doador", "botao": "Salvar Alterações"}
    success_message = "Doador atualizado com sucesso!"


class InstituicaoUpdate(UserObjectPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('instituicaoList')
    extra_context = {'titulo': "Editar Instituição", "botao": "Salvar Alterações"}
    success_message = "Instituição atualizada com sucesso!"


class StatusUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Status
    fields = ['nome', 'pode_editar']
    success_url = reverse_lazy('statusList')
    extra_context = {'titulo': "Editar Status", "botao": "Salvar Alterações"}
    success_message = "Status atualizado com sucesso!"


class DoacaoUpdate(UserObjectPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    fields = ['tipo', 'quantidade', 'data', 'doador', 'instituicao', 'status']
    success_url = reverse_lazy('doacaoList')
    extra_context = {'titulo': "Editar Doação", "botao": "Salvar Alterações"}
    success_message = "Doação atualizada com sucesso!"
    
    def get_queryset(self):
        # Otimizar com select_related para carregar FKs em uma query
        return super().get_queryset().select_related('doador', 'instituicao', 'status')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar doadores do usuário
        if not self.request.user.is_superuser:
            form.fields['doador'].queryset = Doador.objects.filter(
                usuario=self.request.user
            ).only('id', 'nome')
        else:
            form.fields['doador'].queryset = Doador.objects.only('id', 'nome')
        
        # Otimizar querysets
        form.fields['instituicao'].queryset = Instituicao.objects.only('id', 'nome')
        form.fields['status'].queryset = Status.objects.only('id', 'nome')
        return form


class Historia_InspiradorasUpdate(UserObjectPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('historias-inspiradorasList')
    extra_context = {'titulo': "Editar História Inspiradora", "botao": "Salvar Alterações"}
    success_message = "História Inspiradora atualizada com sucesso!"
    
    def get_queryset(self):
        # Otimizar com select_related para carregar FKs em uma query
        return super().get_queryset().select_related('doador', 'instituicao')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar doadores do usuário (campos opcionais)
        if not self.request.user.is_superuser:
            form.fields['doador'].queryset = Doador.objects.filter(
                usuario=self.request.user
            ).only('id', 'nome')
        else:
            form.fields['doador'].queryset = Doador.objects.only('id', 'nome')
        
        # Otimizar queryset de instituições
        form.fields['instituicao'].queryset = Instituicao.objects.only('id', 'nome')
        return form

# ========================================
# VIEWS DE EXCLUSÃO (DELETE)
# ========================================

class DoadorDelete(UserObjectPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doador
    success_url = reverse_lazy('doadorList')
    extra_context = {'titulo': "Excluir Doador", "botao": "Confirmar Exclusão"}
    success_message = "Doador excluído com sucesso!"


class InstituicaoDelete(UserObjectPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    success_url = reverse_lazy('instituicaoList')
    extra_context = {'titulo': "Excluir Instituição", "botao": "Confirmar Exclusão"}
    success_message = "Instituição excluída com sucesso!"


class StatusDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Status
    success_url = reverse_lazy('statusList')
    extra_context = {'titulo': "Excluir Status", "botao": "Confirmar Exclusão"}
    success_message = "Status excluído com sucesso!"


class DoacaoDelete(UserObjectPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    success_url = reverse_lazy('doacaoList')
    extra_context = {'titulo': "Excluir Doação", "botao": "Confirmar Exclusão"}
    success_message = "Doação excluída com sucesso!"


class Historia_InspiradorasDelete(UserObjectPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('historias-inspiradorasList')
    extra_context = {'titulo': "Excluir História Inspiradora", "botao": "Confirmar Exclusão"}
    success_message = "História Inspiradora excluída com sucesso!"

# ========================================
# VIEWS DE LISTAGEM (LIST)
# ========================================

class DoadorList(UserFilterMixin, LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/doadorList.html'
    model = Doador
    context_object_name = 'doadores'
    paginate_by = 20  # Adicionar paginação
    
    def get_queryset(self):
        # Otimizar: apenas campos necessários
        return super().get_queryset().only('id', 'nome', 'telefone', 'cidade').order_by('-id')


class InstituicaoList(UserFilterMixin, LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/instituicaoList.html'
    model = Instituicao
    context_object_name = 'instituicoes'
    paginate_by = 20  # Adicionar paginação
    
    def get_queryset(self):
        # Otimizar: apenas campos necessários
        return super().get_queryset().only(
            'id', 'nome', 'telefone', 'cidade', 'tipo', 'descricao'
        ).order_by('-id')


class DoacaoList(UserFilterMixin, LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/doacaoList.html'
    model = Doacao
    context_object_name = 'doacoes'
    paginate_by = 20  # Adicionar paginação
    
    def get_queryset(self):
        # Otimizar: select_related para evitar N+1 queries
        return super().get_queryset().select_related(
            'doador', 'instituicao', 'status'
        ).only(
            'id', 'tipo', 'quantidade', 'data',
            'doador__nome', 'instituicao__nome', 'status__nome'
        ).order_by('-data')


class Historia_InspiradorasList(UserFilterMixin, LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/historias_inspiradorasList.html'
    model = Historia_Inspiradoras
    context_object_name = 'historias'
    paginate_by = 12  # Adicionar paginação (múltiplo de 3 para grid)
    
    def get_queryset(self):
        # Otimizar: select_related para evitar N+1 queries
        return super().get_queryset().select_related(
            'doador', 'instituicao'
        ).only(
            'id', 'titulo', 'conteudo', 'autor', 'data_postagem',
            'doador__nome', 'instituicao__nome'
        ).order_by('-data_postagem')


class StatusList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/statusList.html'
    model = Status
    context_object_name = 'status_list'
    paginate_by = 20  # Adicionar paginação
    
    def get_queryset(self):
        # Status é global, apenas campos necessários
        return Status.objects.only('id', 'nome', 'pode_editar').order_by('nome')
