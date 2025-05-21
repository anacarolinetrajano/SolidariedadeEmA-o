from django.db import models

tipos_doacao = (
    ("1", "Dinheiro"),
    ("2", "Roupa"),
    ("3", "Alimento"),
)

# Create your models here.

class Doador(models.Model):
    nome = models.CharField(max_length=100) 
    telefone = models.CharField(max_length=14)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=14)
    cidade = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, help_text="Por exemplo: ")
    descricao = models.CharField(max_length=250, verbose_name="descrição")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"
        ordering = ["nome"]

class Status(models.Model):
    nome = models.CharField(max_length=100)
    pode_editar = models.BooleanField(default=True)

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

    def __str__(self):
        return f"[{self.pk}] {self.tipo} - R$ {self.quantidade} ({self.data})"

class Historia_Inspiradoras(models.Model):
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    doador = models.ForeignKey(Doador, on_delete=models.PROTECT, null=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.titulo} ({self.autor})"


