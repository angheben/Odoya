from django.db import models
from stdimage.models import StdImageField


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

    nome = models.CharField(name='Nome', max_length=100)
    preco = models.DecimalField(name='Preço', max_digits=10, decimal_places=2)
    tipo = models.CharField(name='Tipo', max_length=100, choices=tipo_granola)
    peso = models.IntegerField(name='Peso', choices=peso_granola, default=500)
    imagem = StdImageField(name="Imagem", upload_to='imagens_produtos', variations={"thumb": {"width": 500,
                                                                                              "height": 350,
                                                                                              "crop": True}})
