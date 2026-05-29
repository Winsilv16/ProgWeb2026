from django.shortcuts import render, redirect
from loja.models import Produto, Fabricante, Categoria
from django.utils import timezone
from django.core.files.storage import FileSystemStorage


def list_produto_view(request):

    produtos = Produto.objects.all()

    context = {
        'produtos': produtos
    }

    return render(
        request,
        'produto/produtos.html',
        context
    )


def produto_view(request, id):

    produto = Produto.objects.get(id=id)

    context = {
        'produto': produto
    }

    return render(
        request,
        'produto/produto.html',
        context
    )


def create_produto_view(request):

    if request.method == 'POST':

        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        preco = request.POST.get("preco")

        try:

            obj_produto = Produto()

            obj_produto.Produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)

            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao

            obj_produto.preco = 0

            if preco is not None and preco != "":
                obj_produto.preco = preco

            obj_produto.criado_em = timezone.now()
            obj_produto.alterado_em = timezone.now()

            if request.FILES is not None:

                num_files = len(request.FILES.getlist('imagem'))

                if num_files > 0:

                    imagem = request.FILES['imagem']

                    fs = FileSystemStorage()

                    filename = fs.save(imagem.name, imagem)

                    obj_produto.imagem = filename

            obj_produto.save()

            print("Produto salvo com sucesso")

        except Exception as e:
            print("Erro:", e)

        return redirect('/produto')

    fabricantes = Fabricante.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'fabricantes': fabricantes,
        'categorias': categorias
    }

    return render(
        request,
        'produto/produto-create.html',
        context
    )


def edit_produto_view(request, id):

    produto = Produto.objects.get(id=id)

    fabricantes = Fabricante.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'produto': produto,
        'fabricantes': fabricantes,
        'categorias': categorias
    }

    return render(
        request,
        'produto/produto-edit.html',
        context
    )


def edit_produto_postback(request):

    return redirect('/produto')


def delete_produto_view(request, id):

    produto = Produto.objects.get(id=id)

    produto.delete()

    return redirect('/produto')