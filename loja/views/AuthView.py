from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from loja.forms.AuthForm import LoginForm, RegisterForm


def login_view(request):
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        # Instancia o formulário já com os dados do POST
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            # Obtém os dados validados do formulário
            username = loginForm.cleaned_data.get('username')
            password = loginForm.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Resgata a rota protegida enviada via URL (GET) ou via campo oculto (POST)
                _next = request.GET.get('next') or request.POST.get('next')
                if _next:
                    return redirect(_next)
                return redirect('/')
            else:
                message = {'type': 'danger', 'text': 'Dados de usuário incorretos'}
    else:
        loginForm = LoginForm()

    context = {
        'form': loginForm, 
        'message': message, 
        'title': 'Login', 
        'button_text': 'Entrar', 
        'link_text': 'Registrar', 
        'link_href': '/register'
    }
    return render(request, template_name='auth/auth.html', context=context, status=200)


def register_view(request):
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            username = registerForm.cleaned_data.get('username')
            email = registerForm.cleaned_data.get('email')
            password = registerForm.cleaned_data.get('password')

            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()

            if verifyUsername is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com este username!'}
            elif verifyEmail is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com este e-mail!'}
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                if user is not None:
                    message = {'type': 'success', 'text': 'Conta criada com sucesso!'}
                else:
                    message = {'type': 'danger', 'text': 'Um erro ocorreu ao tentar criar o usuário.'}
    else:
        registerForm = RegisterForm()

    context = {
        'form': registerForm, 
        'message': message, 
        'title': 'Registrar', 
        'button_text': 'Registrar', 
        'link_text': 'Login', 
        'link_href': '/login'
    }
    return render(request, template_name='auth/auth.html', context=context, status=200)


def logout_view(request):
    logout(request)
    return redirect('/login')