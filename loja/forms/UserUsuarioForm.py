from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from loja.models.Usuario import Usuario


class UserUsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        # Remove o parâmetro customizado antes de chamar a classe pai
        current_user = kwargs.pop('current_user', None)
        super(UserUsuarioForm, self).__init__(*args, **kwargs)

        # Regra de Segurança: Se não for administrador/superuser, oculta o campo "perfil"
        if current_user and not current_user.is_superuser:
            if self.instance and self.instance.perfil != 1:
                del self.fields['perfil']

    class Meta:
        model = Usuario
        fields = ['user', 'perfil', 'aniversario']
        widgets = {
            'user': forms.HiddenInput(),
            'perfil': forms.Select(attrs={'class': 'form-control'}),
            'aniversario': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }