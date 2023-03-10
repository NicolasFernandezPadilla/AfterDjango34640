from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()
    #datefield format DD/MM/YYYY
    fechaInicio = forms.DateField(input_formats=['%d/%m/%Y'])

class ProfeForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)

class RegistroUsuarioForm(UserCreationForm):
    username=forms.CharField()
    email=forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    

class Meta:
    model= User 
    fields= ["username", "email", "password1", "password2"]
    help_texts= {k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio
