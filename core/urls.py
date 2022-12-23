from django.urls import path
from django.contrib import admin
from .views import IndexViews, ContatoViews, TesteViews

urlpatterns = [
    path('/admin', admin.site.urls),
    path('', IndexViews.as_view(), name="home"),
    path('/contato', ContatoViews.as_view(), name='contato'),
    path('/teste', TesteViews.as_view(), name='teste')
]
