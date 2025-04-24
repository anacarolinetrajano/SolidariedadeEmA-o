from django.db import models

# Create your models here.

class Campus(models.Model):
    nome = models.CharField(max_length=100)

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    campus = models.ForeignKey(Campus,on_delete=models.PROTECT)

 #class TipoSolicitação(models.Model):

    descricao : models.CharField(max_length=250)
    prazo_externo :models.CharField(max_length=250)
    prazo_externo_dias :models.PositiveSmallIntegerField(default=0)
    prazo_interno :models.CharField(max_length=250)
    prazo_interno_dias :models.PositiveSmallIntegerField(default=0)




