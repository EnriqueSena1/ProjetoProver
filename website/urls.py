from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()



urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user/', User.as_view(), name='usuarios'),
    path('api/user/<int:id>', User.as_view(), name="usuarioDetalhe"),
    path('api/login/', Login.as_view(), name='loginAPI'),
    path('api/logout/', Logout.as_view(), name='logout'),
    path('api/cadastrarCompra/', CadastrarCompraView.as_view(), name='CadastrrarCompra'),
    path('api/GetDadosUsuarioLogado', GetDadosUsuarioLogado.as_view(), name='GetDadosUsuarioLogado'),
    path('api/user/historico-saldo/', HistoricoSaldoUsuarioView.as_view(), name='historico-saldo-usuario'),
    path('api/user/<int:id>/historico-saldo/', HistoricoSaldoPorIdView.as_view(), name='historico-saldo-por-id'),
    path('api/usuario/<int:id>/primeiro-acesso/', PrimeiroAcessoSenhaView.as_view(), name='primeiro_acesso_senha'),
    # path('', login, name="login"),
    # path('home/', home, name="home"),
    # path('primeiroAcesso', primeiroAcesso, name="primeiroAcesso"),
    # path('historicoCompra', historicoCompra, name="historicoCompra"),
    # path('listaProdutos', listaProdutos, name="listaProdutos"),
    # path('listaDePedidos', listaDePedidos, name='listaDePedidos'),
    # path('carrinho/', carrinho, name="carrinho"),
    # path('relatorio/', relatorio, name="relatorio"),
    # path('listaEstoque/', listaEstoque, name='listaEstoque'),
    # path('adicionarMoedas/', adicionarMoedas, name='adicionarMoedas'),
    # path('cadastrarUsuario/', cadastrarUsuario, name='cadastrarUsuario'),
    # path('editarUsuario/<int:id>/', editarUsuario, name='editarUsuario'),
    # path('listaDeUsuarios', listaDeUsuarios, name="listaDeUsuarios"),
                      
               
]