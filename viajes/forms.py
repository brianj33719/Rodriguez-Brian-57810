from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class Alojamientosform(forms.Form):
    hotel = forms.CharField(max_length=50, required=True, label="Nombre del Hotel")
    categoriaEstrellas = forms.IntegerField(required=True, label="Categoría en Estrellas")
    
class Paquetesform(forms.Form):
    hotel = forms.CharField(max_length=50, required=True, label="Nombre del Hotel")
    nombreAerolinea = forms.CharField(max_length=50, required=True, label="Nombre de la Aerolínea")
    estadiaNoches = forms.IntegerField(required=True, label="Estadía en noches")
    
class Vuelosform(forms.Form):
    nombreAerolinea = forms.CharField(max_length=50, required=True, label="Nombre de la Aerolínea")

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)  
    password2 = forms.CharField(label = "Confirme la contraseña", widget=forms.PasswordInput)  
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] 

    #para verificar que el usuario y/o el email elegidos no sean existentes:
    def verificarUser(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso. Por favor, elige otro.")
        return username

    def verificarEmail(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso. Por favor, elige otro.")
        return email
    
    def clean_username(self):
        return self.verificarUser()

    def clean_email(self):
        return self.verificarEmail()

#_______________________________#
    
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)