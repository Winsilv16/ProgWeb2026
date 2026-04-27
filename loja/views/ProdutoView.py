from django.http import HttpResponse

def list_produto_view(request, id=None):
    # Trecho opcional do PDF (página 16) incluído conforme solicitado:
    if id is None:
        return HttpResponse('<h1>Nenhum id foi informado</h1>')
        # Ou use: id = 0

    return HttpResponse('<h1>Produto de id %s!</h1>' % id)