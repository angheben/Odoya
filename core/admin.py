from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['Nome', 'Preço', 'Tipo', 'Imagem']


admin.site.register(Produto, ProdutoAdmin)

