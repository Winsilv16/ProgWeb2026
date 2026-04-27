from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Capítulo 5 - Página 9
    path('', include('loja.urls.HomeUrls')),
    # Capítulo 5 - Página 14
    path('produto/', include('loja.urls.ProdutoUrls')),
]

# Configuração de arquivos estáticos (Obrigatório para carregar imagens/CSS)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)