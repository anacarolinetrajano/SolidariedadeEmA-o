from django.urls import path
from .views import (
    PaginaInicial, Sobre,
    DoadorCreate, DoadorUpdate, DoadorDelete,
    InstituicaoCreate, InstituicaoUpdate, InstituicaoDelete,
    DoacaoCreate, DoacaoUpdate, DoacaoDelete,
    StatusCreate, StatusUpdate, StatusDelete,
    Historia_InspiradorasCreate, Historia_InspiradorasUpdate, Historia_InspiradorasDelete, 
    DoadorList, InstituicaoList, DoacaoList, Historia_InspiradorasList, StatusList
)
from .views import CadastroUsuarioView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Rota para o cadastro de usuário
    path("registrar/", CadastroUsuarioView.as_view(), name="registrar"),
    
    path("login/", auth_views.LoginView.as_view(
         template_name = 'paginasweb/form.html', 
          extra_context = {'titulo' : "Autentificação ", "botao" : "Entrar"}
    ), name= "login"),

     path("senha/", auth_views.PasswordChangeView.as_view(
         template_name = 'paginasweb/form.html', 
          extra_context = {'titulo' : "Atualizar ", "botao" : "Salvar"}
    ), name= "senha"),


    #Criar uma rota de logout
    path("sair/", auth_views.LogoutView.as_view(), name= "sair"), 


    path("", PaginaInicial.as_view(), name="index"),
    path("sobre/", Sobre.as_view(), name="sobre"),
    
    path("cadastrar/doador/", DoadorCreate.as_view(), name="cadastrar-doador"),
    path("cadastrar/instituicao/", InstituicaoCreate.as_view(), name="cadastrar-instituicao"),
    path("cadastrar/doacao/", DoacaoCreate.as_view(), name="cadastrar-doacao"),
    path("cadastrar/status/", StatusCreate.as_view(), name="cadastrar-status"),
    path("cadastrar/historia-inspiradora/", Historia_InspiradorasCreate.as_view(), name="cadastrar-historia-inspiradora"),

    path("editar/doador/<int:pk>/",DoadorUpdate.as_view(),name="editar-doador"),
    path("editar/instituicao/<int:pk>/",InstituicaoUpdate.as_view(),name="editar-instituicao"),
    path("editar/doacao/<int:pk>/",DoacaoUpdate.as_view(),name="editar-doacao"),
    path("editar/status/<int:pk>/",StatusUpdate.as_view(),name="editar-status"),
    path("editar/historia-inspiradora/<int:pk>/",Historia_InspiradorasUpdate.as_view(),name="editar-historia-inspiradora"),

    path("deletar/doador/<int:pk>/",DoadorDelete.as_view(),name="deletar-doador"),
    path("deletar/instituicao/<int:pk>/", InstituicaoDelete.as_view(), name="deletar-instituicao"),
    path("deletar/doacao/<int:pk>/", DoacaoDelete.as_view(), name="deletar-doacao"),
    path("deletar/status/<int:pk>/", StatusDelete.as_view(), name="deletar-status"),
    path("deletar/historia-inspiradora/<int:pk>/", Historia_InspiradorasDelete.as_view(), name="deletar-historia-inspiradora"),

    path("listar/doador/", DoadorList.as_view(), name="doadorList"),
    path("listar/instituicao/", InstituicaoList.as_view(), name="instituicaoList"),
    path("listar/doacao/", DoacaoList.as_view(), name="doacaoList"),
    path("listar/status/", StatusList.as_view(), name="statusList"),
    path("listar/historias-inspiradoras/", Historia_InspiradorasList.as_view(), name="historias-inspiradorasList"),


]
