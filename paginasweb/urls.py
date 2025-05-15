from django.urls import path
from .views import (
    DoadorCreateView, DoadorUpdateView, DoadorDeleteView,
    InstituicaoCreateView, InstituicaoUpdateView, InstituicaoDeleteView,
    DoacaoCreateView, DoacaoUpdateView, DoacaoDeleteView,
    StatusCreateView, StatusUpdateView, StatusDeleteView,
    Historia_InspiradorasCreateView, Historia_InspiradorasUpdateView, Historia_InspiradorasDeleteView,
)

urlpatterns = [
    path("cadastrar/doador/", DoadorCreateView.as_view(), name="cadastrar-doador"),
    path("cadastrar/Instituicao/", InstituicaoCreateView.as_view(), name="cadastrar-Instituicao"),
    path("cadastrar/Doacao/", DoacaoCreateView.as_view(), name="cadastrar-Doacao"),
    path("cadastrar/Status/", StatusCreateView.as_view(), name="cadastrar-Status"),
    path("cadastrar/Historia_Inspiradoras/", Historia_InspiradorasCreateView.as_view(), name="cadastrar-Historia_Inspiradoras"),

    path("editar/doador/<int:pk>/",DoadorUpdateView.as_view(),name="editar-doador"),
    path("editar/Instituicao/<int:pk>/",InstituicaoUpdateView.as_view(),name="editar-Instituicao"),
    path("editar/Doacao/<int:pk>/",DoacaoUpdateView.as_view(),name="editar-Doacao"),
    path("editar/Status/<int:pk>/",StatusUpdateView.as_view(),name="editar-Status"),
    path("editar/Historia_Inspiradoras/<int:pk>/",Historia_InspiradorasUpdateView.as_view(),name="editar-Historia_Inspiradoras"),

    path("deletar/doador/<int:pk>/",DoadorDeleteView.as_view(),name="deletar-doador"),
    path("deletar/Instituicao/", InstituicaoDeleteView.as_view(), name="deletar-Instituicao"),
    path("deletar/Doacao/", DoacaoDeleteView.as_view(), name="deletar-Doacao"),
    path("deletar/Status/", StatusDeleteView.as_view(), name="deletar-Status"),
    path("deletar/Historia_Inspiradoras/", Historia_InspiradorasDeleteView.as_view(), name="deletar-Historia_Inspiradoras"),

]
