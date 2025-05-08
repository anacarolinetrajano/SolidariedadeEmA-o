from django.db import models

# Create your models here.

class Campus(models.Model):
    nome = models.CharField(max_length=100) 
    cadastro_em = models.DateTimeField(auto_now_add=True)

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus,on_delete=models.PROTECT)
    cadastro_em = models.DateTimeField(auto_now_add=True)

class TipoSolicitação(models.Model):

    descricao : models.CharField(max_length=250, verbose_name="descrição") # type: ignore
    prazo_externo :models.CharField(max_length=250)
    prazo_externo_dias :models.PositiveSmallIntegerField(default=0)
    prazo_interno :models.CharField(max_length=250)
    prazo_interno_dias :models.PositiveSmallIntegerField(default=0)




