from django.contrib import admin
from .models import *

class FabricanteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Categoria)

class ProdutoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Usuario)