from django.http import HttpResponse

def home(request):
    return HttpResponse("Minha loja está funcionando")