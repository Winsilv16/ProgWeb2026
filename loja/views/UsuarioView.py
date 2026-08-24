from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from loja.models.Usuario import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm


@login_required
def list_usuario_view(request, id=None):
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
        'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context, status=200)


@login_required
def edit_usuario_view(request):
    usuario = Usuario.objects.filter(user=request.user).first()
    emailUnused = True
    message = None

    if request.method == 'POST':
        usuarioForm = UserUsuarioForm(request.POST, instance=usuario, current_user=request.user)
        userForm = UserForm(request.POST, instance=request.user)

        # Leitura com fallback seguro usando .get()
        email_informado = request.POST.get('email', '')

        # Verifica se o e-mail informado já pertence a outro usuário cadastrado
        verifyEmail = Usuario.objects.filter(
            user__email=email_informado
        ).exclude(user__id=request.user.id).first()

        emailUnused = verifyEmail is None
    else:
        usuarioForm = UserUsuarioForm(instance=usuario, current_user=request.user)
        userForm = UserForm(instance=request.user)

    # Processamento e tratamento das mensagens
    if usuarioForm.is_valid() and userForm.is_valid() and emailUnused:
        usuarioForm.save()
        userForm.save()
        message = {'type': 'success', 'text': 'Dados atualizados com sucesso'}
    else:
        if request.method == 'POST':
            if emailUnused:
                message = {'type': 'danger', 'text': 'Dados inválidos'}
            else:
                message = {'type': 'warning', 'text': 'E-mail já usado'}

    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm,
        'message': message
    }
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)