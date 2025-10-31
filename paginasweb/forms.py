from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Doador, Instituicao


# Crie uma classe de formulário para o cadastro de usuários
# A herança é feita para poder tornar o email único e obrigatório
# E outros campos, se necessário
class UsuarioCadastroForm(UserCreationForm):


    email = forms.EmailField(required=True, help_text="Informe um email válido.")


    # Define o model e os fields que vão aparecer na tela
    class Meta:
        model = User
        # Esses dois passwords são para verificar se as senhas são iguais
        fields = ['username', 'email', 'password1', 'password2']


    # O metodo clean no forms serve de validação para os campos
    def clean_email(self):
        # recebe o email do formulário
        email = self.cleaned_data.get('email')
        # Verifica se já existe algum usuário com este email
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email


# Formulário de cadastro de Doador
# Inclui campos de usuário (username, email, senha) + campos do doador (nome, telefone, cidade)
class DoadorCadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Informe um email válido.")
    nome = forms.CharField(max_length=100, required=True, help_text="Nome completo do doador.")
    telefone = forms.CharField(max_length=14, required=True, help_text="Telefone com DDD.")
    cidade = forms.CharField(max_length=100, required=True, help_text="Cidade onde reside.")

    class Meta:
        model = User
        fields = ['nome', 'telefone', 'cidade', 'username', 'email', 'password1', 'password2']
        # remover o autofocus de username
        widgets = {
            'username': forms.TextInput(attrs={'autofocus': False}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def save(self, commit=True):
        # Primeiro salva o usuário
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Depois cria o doador vinculado ao usuário
            Doador.objects.create(
                usuario=user,
                nome=self.cleaned_data['nome'],
                telefone=self.cleaned_data['telefone'],
                cidade=self.cleaned_data['cidade']
            )
        
        return user


# Formulário de cadastro de Instituição
# Inclui campos de usuário (username, email, senha) + campos da instituição
class InstituicaoCadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Informe um email válido.")
    nome = forms.CharField(max_length=150, required=True, help_text="Nome da instituição.")
    telefone = forms.CharField(max_length=14, required=True, help_text="Telefone com DDD.")
    cidade = forms.CharField(max_length=100, required=True, help_text="Cidade onde está localizada.")
    tipo = forms.CharField(max_length=100, required=True, help_text="Tipo: ONG, Abrigo, Hospital, etc.")
    descricao = forms.CharField(
        max_length=250, 
        required=True, 
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text="Breve descrição da instituição e sua missão."
    )

    class Meta:
        model = User
        fields = ['nome', 'telefone', 'cidade', 'tipo', 'descricao', 'username', 'email', 'password1', 'password2']
        # remover o autofocus de username
        widgets = {
            'username': forms.TextInput(attrs={'autofocus': False}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def save(self, commit=True):
        # Primeiro salva o usuário
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Depois cria a instituição vinculada ao usuário
            Instituicao.objects.create(
                usuario=user,
                nome=self.cleaned_data['nome'],
                telefone=self.cleaned_data['telefone'],
                cidade=self.cleaned_data['cidade'],
                tipo=self.cleaned_data['tipo'],
                descricao=self.cleaned_data['descricao']
            )
        
        return user
