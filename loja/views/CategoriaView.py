from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Categoria

def list_categoria_view(request):
    categorias = Categoria.objects.all()
    return render(request, 'categoria/categoria.html', {'categorias': categorias})

def create_categoria_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            Categoria.objects.create(nome=nome)
            return redirect('list_categoria')
    return render(request, 'categoria/categoria-add.html')

def edit_categoria_view(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            categoria.nome = nome
            categoria.save()
            return redirect('list_categoria')
    return render(request, 'categoria/categoria-edit.html', {'categoria': categoria})

def delete_categoria_view(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('list_categoria')
    return render(request, 'categoria/categoria-delete.html', {'categoria': categoria})