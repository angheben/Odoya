from django.urls import path
from .views import IndexViews, ContatoViews, CompraRealizadaViews, InformacoesViews, PedidoViews, SobreViews, \
    PagamentoViews, EnderecoViews, ReceitasViews

urlpatterns = [
    path('', IndexViews.as_view(), name="home"),
    path('compra_realizada.html', CompraRealizadaViews.as_view(), name='compra_realizada'),
    path('contato.html', ContatoViews.as_view(), name='contato'),
    path('endereco.html', EnderecoViews.as_view(), name='endereco'),
    path('informacoes.html', InformacoesViews.as_view(), name='informacoes'),
    path('pagamento.html', PagamentoViews.as_view(), name='pagamento'),
    path('pedido.html', PedidoViews.as_view(), name='pedido'),
    path('receitas.html', ReceitasViews.as_view(), name='receitas'),
    path('sobre.html', SobreViews.as_view(), name='sobre')
]
