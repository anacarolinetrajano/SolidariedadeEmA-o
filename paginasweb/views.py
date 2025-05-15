from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doador, Instituicao, Doacao, Historia_Inspiradoras, Status


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'


class Instituicao(TemplateView):
    template_name = 'paginas/sobre.html'


class DoadorCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Doador
    fields = ['nome', 'email', 'telefone', 'endereco']
    success_url = reverse_lazy('index')

class InstituicaoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Instituicao
    fields = ['nome', 'responsavel', 'email', 'telefone', 'endereco']
    success_url = reverse_lazy('index')


class DoacaoCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Doacao
    fields = ['doador', 'instituicao', 'descricao', 'data', 'status']
    success_url = reverse_lazy('index')

class Historia_InspiradorasCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Historia_Inspiradoras
    fields = ['titulo', 'descricao', 'data', 'autor']
    success_url = reverse_lazy('index')

class StatusCreate(CreateView):
    template_name = 'paginas/form.html'
    model = Status
    fields = ['nome', 'ordem', 'pode_editar']
    success_url = reverse_lazy('index')
    
#############################################################################################################

class DoadorUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Doador
    fields = ['nome', 'email', 'telefone', 'endereco']
    success_url = reverse_lazy('index')

class InstituicaoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Instituicao
    fields = ['nome', 'responsavel', 'email', 'telefone', 'endereco']
    success_url = reverse_lazy('index')


class DoacaoUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Doacao
    fields = ['doador', 'instituicao', 'descricao', 'data', 'status']
    success_url = reverse_lazy('index')

class Historia_InspiradorasUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Historia_Inspiradoras
    fields = ['titulo', 'descricao', 'data', 'autor']
    success_url = reverse_lazy('index')

class StatusUpdate(UpdateView):
    template_name = 'paginas/form.html'
    model = Status
    fields = ['nome', 'ordem', 'pode_editar']
    success_url = reverse_lazy('index')

################################################################################################################

class DoadorDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Doador
    success_url = reverse_lazy('index')

class InstituicaoDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Instituicao
    success_url = reverse_lazy('index')


class DoacaoDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Doacao
    success_url = reverse_lazy('index')

class Historia_InspiradorasDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Historia_Inspiradoras
    success_url = reverse_lazy('index')

class StatusDelete(DeleteView):
    template_name = 'paginas/form.html'
    model = Status
    success_url = reverse_lazy('index')
