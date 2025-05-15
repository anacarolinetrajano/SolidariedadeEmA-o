from django.db import models

# Create your models here.

class Doador(models.Model):
    nome = models.CharField(max_length=100) 
    email = models.CharField(max_length=100)
    telefone = models.PositiveSmallIntegerField(default = 0)
    cidade = models.CharField(max_length=100)

class Instituicao(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    telefone = models.PositiveSmallIntegerField(default = 0)
    cidade = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250, verbose_name="descrição")
    senha = models.CharField(max_length=8)

class Doacao(models.Model):
    tipo = models.CharField(max_length=100)
    quantidade = models.PositiveBigIntegerField(default = 0)
    data = models.DateField

class Status(models.Model):
    nome = models.CharField(max_length=100)
    pode_editar = models.BooleanField("default = true")

class Historia_Inspiradoras(models.Model):
    titulo = models.CharField(max_length=150)
    conteudo = models.CharField(max_length=100)
    data_postagem = models.DateField
    autor = models.CharField(max_length=100)


