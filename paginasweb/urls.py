from django.urls import path
from .views import (
    PaginaInicial, Instituicao,
    DoadorCreate, DoadorUpdate, DoadorDelete,
    InstituicaoCreate, InstituicaoUpdate, InstituicaoDelete,
    DoacaoCreate, DoacaoUpdate, DoacaoDelete,
    StatusCreate, StatusUpdate, StatusDelete,
    Historia_InspiradorasCreate, Historia_InspiradorasUpdate, Historia_InspiradorasDelete,
)

urlpatterns = [
    path("", PaginaInicial.as_view(), name="index"),
    path("", Instituicao.as_view(), name="cadastrar-Instituição"),
    
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
    path("deletar/Instituicao/", InstituicaoDelete.as_view(), name="deletar-Instituicao"),
    path("deletar/Doacao/", DoacaoDelete.as_view(), name="deletar-Doacao"),
    path("deletar/Status/", StatusDelete.as_view(), name="deletar-Status"),
    path("deletar/Historia_Inspiradoras/", Historia_InspiradorasDelete.as_view(), name="deletar-Historia_Inspiradoras"),

]
