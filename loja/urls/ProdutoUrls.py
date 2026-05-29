from django.urls import path

from loja.views.ProdutoView import (
    list_produto_view,
    produto_view,
    create_produto_view,
    edit_produto_view,
    edit_produto_postback,
    delete_produto_view
)

urlpatterns = [

    path(
        '',
        list_produto_view,
        name='produto'
    ),

    path(
        '<int:id>/',
        produto_view,
        name='produto_view'
    ),

    path(
        'create/',
        create_produto_view,
        name='create_produto'
    ),

    path(
        'edit/<int:id>/',
        edit_produto_view,
        name='edit_produto'
    ),

    path(
        'edit/postback/',
        edit_produto_postback,
        name='edit_produto_postback'
    ),

    path(
        'delete/<int:id>/',
        delete_produto_view,
        name='delete_produto'
    )
]