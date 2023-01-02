from django.views.generic import TemplateView, FormView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Produto


class IndexView(TemplateView):
    template_name = 'home.html'


class ContatoView(IndexView):
    template_name = 'contato.html'


class CompraRealizadaView(IndexView):
    template_name = 'compra_realizada_views.html'


class EnderecoView(IndexView):
    template_name = 'endereco.html'


class InformacoesView(IndexView):
    template_name = 'informacoes.html'


class PagamentoView(IndexView):
    template_name = 'pagamento.html'


class PedidoView(ListView):
    template_name = 'pedido.html'
    queryset = Produto.objects.all()


class ListaView(ListView):
    template_name = 'lista.html'
    model = Produto
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class AdicionarProdutoView(CreateView):
    template_name = 'adicionar_produto.html'
    model = Produto
    fields = ['nome', 'preco', 'tipo', 'peso', 'imagem']
    success_url = reverse_lazy('lista')


class AtualizarProdutoView(UpdateView):
    template_name = 'atualizar_produto.html'
    model = Produto
    fields = ['nome', 'preco', 'tipo', 'peso', 'imagem']
    success_url = reverse_lazy('lista')


class DeletarProdutoView(DeleteView):
    template_name = 'deletar_produto.html'
    model = Produto
    success_url = reverse_lazy('lista')


class ReceitasView(IndexView):
    template_name = 'receitas.html'


class SobreView(IndexView):
    template_name = 'sobre.html'
