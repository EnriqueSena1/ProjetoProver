from rest_framework import serializers
from .models import *

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser 
        fields = '__all__' 

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'

class ItensCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = '__all__'

class HistoricoSaldo(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='historico_saldo')
    saldo_anterior = models.IntegerField()
    saldo_novo = models.IntegerField()
    diferenca = models.IntegerField()
    data_alteracao = models.DateTimeField()

    class Meta:
        ordering = ['-data_alteracao']

    def is_positivo(self):
        return self.diferenca >= 0

    def __str__(self):
        sinal = '+' if self.is_positivo() else ''
        return f"{self.usuario.username}: {sinal}{self.diferenca} em {self.data_alteracao.strftime('%Y-%m-%d %H:%M')}"
    
class HistoricoSaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSaldo
        fields = ['saldo_anterior', 'saldo_novo', 'diferenca', 'data_alteracao']

class UsuarioComHistoricoSerializer(serializers.ModelSerializer):
    ultimas_alteracoes = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'saldo', 'ultimas_alteracoes']

    def get_ultimas_alteracoes(self, obj):
        queryset = obj.historico_saldo.all()[:5]
        return HistoricoSaldoSerializer(queryset, many=True).data