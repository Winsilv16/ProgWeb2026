from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Fabricante
from loja.forms.FabricanteForm import FabricanteForm

def list_fabricante_view(request):
    fabricantes = Fabricante.objects.all()
    return render(request, 'fabricante/fabricante.html', {'fabricantes': fabricantes})

def add_fabricante_view(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_fabricante')
    else:
        form = FabricanteForm()
    return render(request, 'fabricante/fabricante-add.html', {'form': form})

def edit_fabricante_view(request, id):
    fabricante = get_object_or_404(Fabricante, id=id)
    if request.method == 'POST':
        form = FabricanteForm(request.POST, instance=fabricante)
        if form.is_valid():
            form.save()
            return redirect('list_fabricante')
    else:
        form = FabricanteForm(instance=fabricante)
    return render(request, 'fabricante/fabricante-edit.html', {'form': form})

def delete_fabricante_view(request, id):
    fabricante = get_object_or_404(Fabricante, id=id)
    if request.method == 'POST':
        fabricante.delete()
        return redirect('list_fabricante')
    return render(request, 'fabricante/fabricante-delete.html', {'fabricante': fabricante})