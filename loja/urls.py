from django.urls import path
from loja.views import UsuarioView, AuthView, ProdutoView

urlpatterns = [
    
    path('login/', AuthView.login_view, name='login'),
    path('register/', AuthView.register_view, name='register'),
    path('logout/', AuthView.logout_view, name='logout'),  # <-- Rota que estava faltando ou sem o nome 'logout'

    path('usuario/', UsuarioView.perfil_view, name='usuario'),
    path('usuario/edit/', UsuarioView.edit_perfil_view, name='edit_usuario'),

    path('produto/edit/<int:id>/', ProdutoView.edit_produto_view, name='edit_produto'),
]