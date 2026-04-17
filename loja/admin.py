from django.contrib import admin

from .models.Fabricante import Fabricante
from .models.Categoria import Categoria
from .models.Produto import Produto

admin.site.register(Fabricante)
admin.site.register(Categoria)
admin.site.register(Produto)