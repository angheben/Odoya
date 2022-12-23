from django.shortcuts import render
from django.views.generic import TemplateView


class IndexViews(TemplateView):
    template_name = 'home.html'


class ContatoViews(IndexViews):
    template_name = 'contato.html'


class TesteViews(IndexViews):
    template_name = 'teste.html'
