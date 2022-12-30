from django.db import models
from stdimage.models import StdImageField
from stdimage.utils import render_variations


class Base(models.Model):
    creation = models.DateField('Creation', auto_now_add=True)
    modification = models.DateField('Atualization', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    doce = 'Doce'
    salgado = 'Salgado'

    tipo_granola = [
        (doce, "Doce"),
        (salgado, 'Salgado')
    ]

    peso_granola = [
        (200, '200'),
        (300, '300'),
        (500, '500'),
        (850, '850'),
        (1000, '1000')
    ]

    nome = models.CharField(name='nome', max_length=100)
    preco = models.DecimalField(name='preco', max_digits=10, decimal_places=2)
    tipo = models.CharField(name='tipo', max_length=100, choices=tipo_granola)
    peso = models.IntegerField(name='peso', choices=peso_granola, default=500)
    imagem = StdImageField(name="imagem", upload_to='imagens_produtos',
                           variations={'thumb': {'width': 100, 'height': 150, 'crop': False}})

    def __str__(self):
        return self.nome
