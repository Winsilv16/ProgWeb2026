from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from loja.models import Carrinho, CarrinhoItem, Produto

def create_carrinhoitem_view(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho_id = request.session.get('carrinho_id')

    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id, situacao=0).first()
    else:
        carrinho = None

    if not carrinho:
        carrinho = Carrinho.objects.create()
        request.session['carrinho_id'] = carrinho.id

    item, created = CarrinhoItem.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
        defaults={'preco': produto.preco, 'quantidade': 1}
    )

    if not created:
        item.quantidade += 1
        item.save()

    return redirect('list_carrinho')

def list_carrinho_view(request):
    carrinho_id = request.session.get('carrinho_id')
    itens = []
    carrinho = None

    if carrinho_id:
        carrinho = Carrinho.objects.filter(id=carrinho_id, situacao=0).first()
        if carrinho:
            itens = CarrinhoItem.objects.filter(carrinho=carrinho)

    return render(request, 'carrinho/carrinho-listar.html', {'carrinho': carrinho, 'itens': itens})

def remover_item_view(request, item_id):
    if request.method == 'POST':
        carrinho_id = request.session.get('carrinho_id')
        if carrinho_id:
            item = get_object_or_404(CarrinhoItem, id=item_id, carrinho_id=carrinho_id)
            item.delete()
    return redirect('list_carrinho')

@login_required
def confirmar_carrinho_view(request):
    carrinho_id = request.session.get('carrinho_id')
    if not carrinho_id:
        return redirect('list_carrinho')

    carrinho = get_object_or_404(Carrinho, id=carrinho_id, situacao=0)
    carrinho.user = request.user
    carrinho.situacao = 1
    carrinho.confirmado_em = timezone.make_aware(timezone.datetime.now())
    carrinho.save()

    del request.session['carrinho_id']
    return render(request, 'carrinho/carrinho-confirmado.html', {'carrinho': carrinho})