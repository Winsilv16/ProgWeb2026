from django.urls import path
from loja.views import CategoriaView

urlpatterns = [
    path('', CategoriaView.list_categoria_view, name='list_categoria'),
    path('add/', CategoriaView.create_categoria_view, name='add_categoria'),
    path('edit/<int:id>/', CategoriaView.edit_categoria_view, name='edit_categoria'),
    path('delete/<int:id>/', CategoriaView.delete_categoria_view, name='delete_categoria'),
]