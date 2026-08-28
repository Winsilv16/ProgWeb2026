from django.shortcuts import render
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
    message = None

    if request.method == 'POST':
        usuarioForm = UserUsuarioForm(request.POST, instance=usuario, current_user=request.user)
        userForm = UserForm(request.POST, instance=request.user)

        email_informado = request.POST.get('email', '')

        verifyEmail = Usuario.objects.filter(
            user__email=email_informado
        ).exclude(user__id=request.user.id).first()

        emailUnused = verifyEmail is None

        if usuarioForm.is_valid() and userForm.is_valid() and emailUnused:
            usuarioForm.save()
            userForm.save()
            message = {'type': 'success', 'text': 'Dados atualizados com sucesso'}
        else:
            if emailUnused:
                message = {'type': 'danger', 'text': 'Dados inválidos'}
            else:
                message = {'type': 'warning', 'text': 'E-mail já usado'}
    else:
        usuarioForm = UserUsuarioForm(instance=usuario, current_user=request.user)
        userForm = UserForm(instance=request.user)

    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm,
        'message': message
    }
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)