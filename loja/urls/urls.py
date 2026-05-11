from django.urls import path
from .views.ProdutoView import listar_produtos

urlpatterns = [
    path('', listar_produtos),
]