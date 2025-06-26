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

from django.contrib.auth import views as auth_views

urlpatterns = [
    #Criar rota para página de login
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
    path("cadastrar/Instituicao/", InstituicaoCreate.as_view(), name="cadastrar-Instituicao"),
    path("cadastrar/Doacao/", DoacaoCreate.as_view(), name="cadastrar-Doacao"),
    path("cadastrar/Status/", StatusCreate.as_view(), name="cadastrar-Status"),
    path("cadastrar/Historia_Inspiradoras/", Historia_InspiradorasCreate.as_view(), name="cadastrar-Historia_Inspiradoras"),

    path("editar/doador/<int:pk>/",DoadorUpdate.as_view(),name="editar-doador"),
    path("editar/Instituicao/<int:pk>/",InstituicaoUpdate.as_view(),name="editar-Instituicao"),
    path("editar/Doacao/<int:pk>/",DoacaoUpdate.as_view(),name="editar-Doacao"),
    path("editar/Status/<int:pk>/",StatusUpdate.as_view(),name="editar-Status"),
    path("editar/Historia_Inspiradoras/<int:pk>/",Historia_InspiradorasUpdate.as_view(),name="editar-Historia_Inspiradoras"),

    path("deletar/doador/<int:pk>/",DoadorDelete.as_view(),name="deletar-doador"),
    path("deletar/Instituicao/<int:pk>/", InstituicaoDelete.as_view(), name="deletar-Instituicao"),
    path("deletar/Doacao/<int:pk>/", DoacaoDelete.as_view(), name="deletar-Doacao"),
    path("deletar/Status/<int:pk>/", StatusDelete.as_view(), name="deletar-Status"),
    path("deletar/Historia_Inspiradoras/<int:pk>/", Historia_InspiradorasDelete.as_view(), name="deletar-Historia_Inspiradoras"),

    path("listar/doador/", DoadorList.as_view(), name="listar-doador"),
    path("listar/Instituicao/", InstituicaoList.as_view(), name="listar-Instituicao"),
    path("listar/Doacao/", DoacaoList.as_view(), name="listar-Doacao"),
    path("listar/Status/", StatusList.as_view(), name="listar-Status"),
    path("listar/Historia_Inspiradoras/", Historia_InspiradorasList.as_view(), name="listar-Historia_Inspiradoras"),


]
