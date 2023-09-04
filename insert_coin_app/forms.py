from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SociosForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    edad = forms.IntegerField(required=True)

class RegistroUsuariosForm(UserCreationForm):
    email = forms.EmailField(max_length=40, label='Email de Usuario', required=True)
    name = forms.CharField(label="Nombre", required=True, max_length=50)
    last_name = forms.CharField(label="Apellido", required=True, max_length=50)
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password1= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'name', 'last_name', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=40, label='Email de Usuario')
    name = forms.CharField(label="Nombre", max_length=50)
    last_name = forms.CharField(label="Apellido")
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password1= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'password1', 'password2']


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)