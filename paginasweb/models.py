# FileName: MultipleFiles/models.py
from django.db import models
from django.contrib.auth.models import User # Ensure User is imported

tipos_doacao = (
    ("1", "Dinheiro"),
    ("2", "Roupa"),
    ("3", "Alimento"),
)

class Doador(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    cidade = models.CharField(max_length=100)
    # Add ForeignKey to User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=14)
    cidade = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, help_text="Por exemplo: ONG, Abrigo, Hospital")
    descricao = models.CharField(max_length=250, verbose_name="descrição")
    # Add ForeignKey to User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

    # Corrected Meta class placement
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"
        ordering = ["nome"]

class Status(models.Model):
    nome = models.CharField(max_length=100)
    pode_editar = models.BooleanField(default=True)
    # Status might not need a user, as it could be a global setting.
    # If you want users to manage their own statuses, add:
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if(self.pode_editar):
            return f"{self.nome} - (Editável)"
        else:
            return f"{self.nome} - (Não poderá ser atualizado)"

class Doacao(models.Model):
    tipo = models.CharField(max_length=100, choices=tipos_doacao)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField()
    doador = models.ForeignKey(Doador, on_delete=models.PROTECT)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    # Add ForeignKey to User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"[{self.pk}] {self.get_tipo_display()} - {self.quantidade} ({self.data.strftime('%d/%m/%Y')})"

class Historia_Inspiradoras(models.Model):
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    doador = models.ForeignKey(Doador, on_delete=models.PROTECT, null=True, blank=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT, null=True, blank=True)
    # Add ForeignKey to User
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True) # Changed to PROTECT as it relates to Doador/Instituicao

    def __str__(self):
        return f"{self.titulo} ({self.autor})"
