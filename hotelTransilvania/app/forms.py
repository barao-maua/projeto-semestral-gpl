from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Usuário')
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

    class Meta:
        model = Usuario
        fields = ['cpf', 'nome', 'email','telefone', 'genero', 'data_nascimento'] 

        widgets = {
            'senha': forms.PasswordInput(),
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
