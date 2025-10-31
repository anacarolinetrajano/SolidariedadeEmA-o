# FileName: MultipleFiles/views.py
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User, Group

from .models import Doador, Instituicao, Status, Doacao, Historia_Inspiradoras
from .forms import UsuarioCadastroForm, DoadorCadastroForm, InstituicaoCadastroForm


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

# Views para Páginas Estáticas
class PaginaInicial(TemplateView):
    template_name = 'paginasweb/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Buscar últimas 3 instituições cadastradas
        context['ultimas_instituicoes'] = Instituicao.objects.all().order_by('-id')[:3]
        # Buscar últimas 5 histórias cadastradas
        context['ultimas_historias'] = Historia_Inspiradoras.objects.all().order_by('-data_postagem')[:5]
        return context

class Sobre(TemplateView):
    template_name = 'paginasweb/sobre.html'

# View pública para listar todas as instituições
class InstituicoesPublicasList(ListView):
    template_name = 'paginasweb/instituicoes_publicas.html'
    model = Instituicao
    context_object_name = 'instituicoes'
    paginate_by = 9  # 9 cards por página (3x3)
    
    def get_queryset(self):
        # Lista todas as instituições para visualização pública
        return Instituicao.objects.all().order_by('-id')


class HistoriasPublicasList(ListView):
    template_name = 'paginasweb/historias_publicas.html'
    model = Historia_Inspiradoras
    context_object_name = 'historias'
    paginate_by = 9  # 9 cards por página (3x3)
    
    def get_queryset(self):
        # Lista todas as histórias para visualização pública
        return Historia_Inspiradoras.objects.all().order_by('-data_postagem')

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
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar apenas doadores e instituições do usuário atual (exceto superuser)
        if not self.request.user.is_superuser:
            form.fields['doador'].queryset = Doador.objects.filter(usuario=self.request.user)
        return form

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
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar doadores e instituições do usuário (campos opcionais)
        if not self.request.user.is_superuser:
            form.fields['doador'].queryset = Doador.objects.filter(usuario=self.request.user)
        # Tornar autor opcional ou preencher automaticamente com username
        form.fields['autor'].initial = self.request.user.username
        return form

# Views para Atualização (Update) - Modified to filter by current user
class DoadorUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Doador
    fields = ['nome', 'telefone', 'cidade']
    success_url = reverse_lazy('doadorList')
    extra_context = {'titulo' : "Editar Doador", "botao" : "Salvar Alterações"}
    success_message = "Doador atualizado com sucesso!"

    def get_object(self):
        # Permite edição apenas de registros do usuário atual (ou todos se for superuser)
        if self.request.user.is_superuser:
            return Doador.objects.get(pk=self.kwargs["pk"])
        return Doador.objects.get(usuario=self.request.user, pk=self.kwargs["pk"])

class InstituicaoUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao']
    success_url = reverse_lazy('instituicaoList')
    extra_context = {'titulo' : "Editar Instituição", "botao" : "Salvar Alterações"}
    success_message = "Instituição atualizada com sucesso!"

    def get_object(self):
        # Permite edição apenas de registros do usuário atual (ou todos se for superuser)
        if self.request.user.is_superuser:
            return Instituicao.objects.get(pk=self.kwargs["pk"])
        return Instituicao.objects.get(usuario=self.request.user, pk=self.kwargs["pk"])

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

    def get_object(self):
        # Permite edição apenas de registros do usuário atual (ou todos se for superuser)
        if self.request.user.is_superuser:
            return Doacao.objects.get(pk=self.kwargs["pk"])
        return Doacao.objects.get(usuario=self.request.user, pk=self.kwargs["pk"])
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar doadores e instituições do usuário
        if not self.request.user.is_superuser:
            form.fields['doador'].queryset = Doador.objects.filter(usuario=self.request.user)
        return form

class Historia_InspiradorasUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    fields = ['titulo', 'conteudo', 'autor', 'doador', 'instituicao']
    success_url = reverse_lazy('historias-inspiradorasList')
    extra_context = {'titulo' : "Editar História Inspiradora", "botao" : "Salvar Alterações"}
    success_message = "História Inspiradora atualizada com sucesso!"

    def get_object(self):
        # Permite edição apenas de registros do usuário atual (ou todos se for superuser)
        if self.request.user.is_superuser:
            return Historia_Inspiradoras.objects.get(pk=self.kwargs["pk"])
        return Historia_Inspiradoras.objects.get(usuario=self.request.user, pk=self.kwargs["pk"])
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Filtrar doadores e instituições do usuário (campos opcionais)
        if not self.request.user.is_superuser:
            form.fields['doador'].queryset = Doador.objects.filter(usuario=self.request.user)
        return form

# Views para Exclusão (Delete) - Modified to filter by current user
class DoadorDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doador
    success_url = reverse_lazy('doadorList')
    extra_context = {'titulo' : "Excluir Doador", "botao" : "Confirmar Exclusão"}
    success_message = "Doador excluído com sucesso!"
    
    def get_object(self):
        # Permite exclusão apenas de registros do usuário atual (ou todos se for superuser)
        if self.request.user.is_superuser:
            return Doador.objects.get(pk=self.kwargs["pk"])
        return Doador.objects.get(usuario=self.request.user, pk=self.kwargs["pk"])
    
class InstituicaoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Instituicao
    success_url = reverse_lazy('instituicaoList')
    extra_context = {'titulo' : "Excluir Instituição", "botao" : "Confirmar Exclusão"}
    success_message = "Instituição excluída com sucesso!"
    
    def get_object(self):
        # Permite exclusão apenas de registros do usuário atual (ou todos se for superuser)
        if self.request.user.is_superuser:
            return Instituicao.objects.get(pk=self.kwargs["pk"])
        return Instituicao.objects.get(usuario=self.request.user, pk=self.kwargs["pk"])


class StatusDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Status
    success_url = reverse_lazy('statusList')
    extra_context = {'titulo' : "Excluir Status", "botao" : "Confirmar Exclusão"}
    success_message = "Status excluído com sucesso!"
    

class DoacaoDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'paginasweb/form.html'
    model = Doacao
    success_url = reverse_lazy('doacaoList')
    extra_context = {'titulo' : "Excluir Doação", "botao" : "Confirmar Exclusão"}
    success_message = "Doação excluída com sucesso!"
    
    def get_object(self):
        # Permite exclusão apenas de registros do usuário atual (ou todos se for superuser)
        if self.request.user.is_superuser:
            return Doacao.objects.get(pk=self.kwargs["pk"])
        return Doacao.objects.get(usuario=self.request.user, pk=self.kwargs["pk"])

class Historia_InspiradorasDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Historia_Inspiradoras
    template_name = 'paginasweb/form.html'
    success_url = reverse_lazy('historias-inspiradorasList')
    extra_context = {'titulo' : "Excluir História Inspiradora", "botao" : "Confirmar Exclusão"}
    success_message = "História Inspiradora excluída com sucesso!"
    
    def get_object(self):
        # Permite exclusão apenas de registros do usuário atual (ou todos se for superuser)
        if self.request.user.is_superuser:
            return Historia_Inspiradoras.objects.get(pk=self.kwargs["pk"])
        return Historia_Inspiradoras.objects.get(usuario=self.request.user, pk=self.kwargs["pk"])

# Views para Listagem (List) - Modified to filter by current user
class DoadorList(LoginRequiredMixin, ListView):
        template_name = 'paginasweb/lista/doadorList.html'
        model = Doador
        context_object_name = 'doadores'
        
        def get_queryset(self):
            # Lista apenas registros do usuário atual ou todos se for superuser
            if self.request.user.is_superuser:
                return Doador.objects.all()
            return Doador.objects.filter(usuario=self.request.user)

class InstituicaoList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/instituicaoList.html'
    model = Instituicao
    context_object_name = 'instituicoes'

    def get_queryset(self):
        # Lista apenas registros do usuário atual ou todos se for superuser
        if self.request.user.is_superuser:
            return Instituicao.objects.all()
        return Instituicao.objects.filter(usuario=self.request.user)

class DoacaoList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/doacaoList.html'
    model = Doacao
    context_object_name = 'doacoes'

    def get_queryset(self):
        # Lista apenas registros do usuário atual ou todos se for superuser
        if self.request.user.is_superuser:
            return Doacao.objects.all()
        return Doacao.objects.filter(usuario=self.request.user)

class Historia_InspiradorasList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/historias_inspiradorasList.html'
    model = Historia_Inspiradoras
    context_object_name = 'historias'

    def get_queryset(self):
        # Lista apenas registros do usuário atual ou todos se for superuser
        if self.request.user.is_superuser:
            return Historia_Inspiradoras.objects.all()
        return Historia_Inspiradoras.objects.filter(usuario=self.request.user)

class StatusList(LoginRequiredMixin, ListView):
    template_name = 'paginasweb/lista/statusList.html'
    model = Status
    context_object_name = 'status_list'
    
    def get_queryset(self):
        # Status é global, então mostra todos
        return Status.objects.all()
