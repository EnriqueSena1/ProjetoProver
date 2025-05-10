from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    is_adm = models.BooleanField(default=False)
    cpf = models.CharField(max_length=11, default=False)


class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    cpf = models.CharField(max_length= 11, default=False)
    tell = models.CharField(max_length= 11, null=False, default=False)

class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    marca = models.CharField(max_length=50, null=False, default=False)
    qtd_prod = models.IntegerField(null=False, blank=False)
    valor = models.IntegerField (null=False, blank=False)
    tipo_choices = [("Perecivel","Perecivel"), ("Congelado","Congelado"), ("Não Pereciveis", "Não Pereciveis")]
    tipo_prod = models.CharField(max_length=16, choices = tipo_choices)
    descricao_pro = models.TextField(max_length=350 )
    img_prod = models.CharField(max_length=150, null=False, default= False)
    
class Carrinho(models.Model):
    idProduto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=False, blank=False)
    qtd_carrinho = models.IntegerField(null=False, blank=False)
    valor_carrinho = models.IntegerField (null=False, blank=False)

class Compra(models.Model):
    total = models.IntegerField(null=False, blank=False)
    pedido_choices = [("Pendente", "Pendente"), ("Concluído","Concluído")]
    pedido = models.CharField(max_length=10, choices=pedido_choices, default='Pendente')
    dataCompra = models.DateTimeField(auto_now_add=True)
    idUsuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    idVendedor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)

class ItensCompra(models.Model):
    idCarrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, null=False, blank=False)
    idVendedor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False, blank=False) 
    valor_total = models.IntegerField(null=False, blank=False)