from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    is_adm = models.BooleanField(default=False)
    cpf = models.CharField(max_length=11, default=False)


class Cliente(models.Model):
    nome = models.models.CharField(max_length=50, null=False, blank=False)
    cpf = models.CharField(max_length= 11, default=False)
    tell = models.CharField(max_length= 11, null=False, default=False)

class Produto(models.Model):
    nome = models.models.CharField(max_length=50, null=False, blank=False)
    qtd_prod = models.IntegerField(null=False, blank=False)
    valor = models.IntegerField (null=False, blank=False)
    tipo_choices = [("Perecivel","Perecivel"), ("Congelado","Congelado"), ("Não Pereciveis", "Não Pereciveis")]
    tipo_prod = models.CharField(max_length=16, choices = tipo_choices)
    descricao = models.TextField()
    img_prod = models.models.CharField(max_length=150, null=False, default= False)


    