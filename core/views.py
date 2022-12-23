from django.views.generic import TemplateView


class IndexViews(TemplateView):
    template_name = 'home.html'


class ContatoViews(IndexViews):
    template_name = 'contato.html'


class CompraRealizadaViews(IndexViews):
    template_name = 'compra_realizada_views.html'


class EnderecoViews(IndexViews):
    template_name = 'endereco.html'


class InformacoesViews(IndexViews):
    template_name = 'informacoes.html'


class PagamentoViews(IndexViews):
    template_name = 'pagamento.html'


class PedidoViews(IndexViews):
    template_name = 'pedido.html'


class ReceitasViews(IndexViews):
    template_name = 'receitas.html'


class SobreViews(IndexViews):
    template_name = 'sobre.html'
