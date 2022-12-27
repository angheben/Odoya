from django.urls import path
from .views import IndexView, ContatoView, CompraRealizadaView, InformacoesView, PedidoView, SobreView, \
    PagamentoView, EnderecoView, ReceitasView, AdicionarProdutoView, AtualizarProdutoView, DeletarProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('compra_realizada.html', CompraRealizadaView.as_view(), name='compra_realizada'),
    path('contato.html', ContatoView.as_view(), name='contato'),
    path('endereco.html', EnderecoView.as_view(), name='endereco'),
    path('informacoes.html', InformacoesView.as_view(), name='informacoes'),
    path('pagamento.html', PagamentoView.as_view(), name='pagamento'),

    path('pedido.html', PedidoView.as_view(), name='pedido'),
    path('adicionar_produto.html', AdicionarProdutoView.as_view(), name='adicionar_produto'),
    path('<int:pk>/atualizar_produto.html', AtualizarProdutoView.as_view(), name='atualizar_produto'),
    path('<int:pk>/deletar_produto.html', DeletarProdutoView.as_view(), name='deletar_produto'),

    path('receitas.html', ReceitasView.as_view(), name='receitas'),
    path('sobre.html', SobreView.as_view(), name='sobre')
]
