from django import forms
from .models import Usuario, AvaliacaoUsuario, Reserva

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        label='Usuário',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Digite seu nome de usuário'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Digite sua senha'
        }),
        label='Senha'
    )

    class Meta:
        model = Usuario
        fields = ['cpf', 'nome', 'email','telefone', 'genero', 'data_nascimento']

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'nome': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'telefone': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'genero': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'data_nascimento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 border rounded-lg'
            }),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Usuário',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Digite seu nome de usuário'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Digite sua senha'
        }),
        label='Senha'
    )

class AvaliacaoUsuarioForm(forms.ModelForm):
    nota = forms.DecimalField(min_value=0.0, max_value=5.0, max_digits=2, decimal_places=1, label='Nota (0 - 5)',widget=forms.NumberInput(attrs={
            'class': 'w-1/3 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
        }))
    
    comentario = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Deixe seu comentário...'
        }))

    class Meta:
        model = AvaliacaoUsuario
        fields = ['nota', 'comentario']

        widget=forms.NumberInput(attrs={
            'type': 'range',
            'step': '0.1',
            'min': '0',
            'max': '5'
        })

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['data_inicio', 'data_fim']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Defina os campos como somente leitura
            self.fields['data_inicio'].widget.attrs['readonly'] = True
            self.fields['data_fim'].widget.attrs['readonly'] = True