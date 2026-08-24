from django.urls import path
from loja.views import FabricanteView

urlpatterns = [
    path('', FabricanteView.list_fabricante_view, name='list_fabricante'),
    path('add/', FabricanteView.add_fabricante_view, name='add_fabricante'),
    path('edit/<int:id>/', FabricanteView.edit_fabricante_view, name='edit_fabricante'),
    path('delete/<int:id>/', FabricanteView.delete_fabricante_view, name='delete_fabricante'),
]