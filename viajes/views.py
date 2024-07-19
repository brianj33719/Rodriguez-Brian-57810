from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *

from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

 
from django.contrib.auth.mixins import LoginRequiredMixin #trabajan sobre las clases 
from django.contrib.auth.decorators import login_required #trabajan sobre las funciones
 
def home(request):
    return render(request, "viajes/index.html")

def acerca(request):
    return render(request, "viajes/acerca.html")

#___ Agrupación por modelos___:


#___ Alojamientos___:
def alojamientos(request):
    contexto = {"alojamientos": Alojamientos.objects.all()}
    return render(request, "viajes/alojamientos.html", contexto)
#no requiere login

@login_required
def alojamientosform(request):
    if request.method == "POST":
        miForm = Alojamientosform(request.POST)
        if miForm.is_valid():
            alojamientos_hotel = miForm.cleaned_data.get("hotel")
            alojamientos_estrellas = miForm.cleaned_data.get("categoriaEstrellas")
            alojamientos = Alojamientos(hotel=alojamientos_hotel, categoriaEstrellas=alojamientos_estrellas)
            alojamientos.save()
            contexto = {"alojamientos": Alojamientos.objects.all()}
            return render(request, "viajes/alojamientos.html", contexto) 
    else:
        miForm = Alojamientosform()
         
    return render(request, "viajes/alojamientosForm.html", {"form": miForm})

def buscarAlojamientos(request):
    return render(request, "viajes/buscar.html" )
#no requiere login

def encontrarAlojamientos(request):
    if request.GET["buscar"]:
        metodo = request.GET["buscar"]
        alojamientos = Alojamientos.objects.filter(hotel__icontains=metodo)
        contexto = {"alojamientos": alojamientos}
    else:
        contexto = {"alojamientos": Alojamientos.objects.all()}
        
    return render(request, "viajes/alojamientos.html", contexto)
#no requiere login

@login_required
def alojamientosUpdate(request, id_alojamiento):
    alojamiento = Alojamientos.objects.get(id=id_alojamiento)
    if request.method == "POST":
        miForm = Alojamientosform(request.POST)
        if miForm.is_valid():
            alojamiento.hotel = miForm.cleaned_data.get("hotel")
            alojamiento.categoriaEstrellas = miForm.cleaned_data.get("categoriaEstrellas")
            alojamiento.save()
            contexto = { "alojamientos": Alojamientos.objects.all() }
            return render(request, "viajes/alojamientos.html", contexto)            
    else:
        miForm = Alojamientosform(initial={"hotel": alojamiento.hotel, "categoriaEstrellas": alojamiento.categoriaEstrellas})

    return render(request, "viajes/alojamientosForm.html", {"form": miForm})

@login_required
def alojamientosDelete(request, id_alojamiento):
    alojamiento = Alojamientos.objects.get(id=id_alojamiento)
    alojamiento.delete()
    contexto = { "alojamientos": Alojamientos.objects.all() }
    return render(request, "viajes/alojamientos.html", contexto)


#___ Paquetes___:
def paquetes(request):
    contexto = {"paquetes": Paquetes.objects.all()}
    return render(request, "viajes/paquetes.html", contexto)
#no requiere login

@login_required
def paquetesform(request):
    if request.method == "POST":
        miForm = Paquetesform(request.POST)
        if miForm.is_valid():
            paquetes_hotel = miForm.cleaned_data.get("hotel")
            paquetes_nombreAerolinea = miForm.cleaned_data.get("nombreAerolinea")
            paquetes_estadiaNoches = miForm.cleaned_data.get("estadiaNoches")
            paquetes = Paquetes(hotel=paquetes_hotel, nombreAerolinea=paquetes_nombreAerolinea, estadiaNoches=paquetes_estadiaNoches)
            paquetes.save()
            contexto = {"paquetes": Paquetes.objects.all()}
            return render(request, "viajes/paquetes.html", contexto) 
    else:
        miForm = Paquetesform()
         
    return render(request, "viajes/paquetesForm.html", {"form": miForm})

@login_required
def paquetesUpdate(request, id_paquete):
    paquete = Paquetes.objects.get(id=id_paquete)
    if request.method == "POST":
        miForm = Paquetesform(request.POST)
        if miForm.is_valid():
            paquete.hotel = miForm.cleaned_data.get("hotel")
            paquete.nombreAerolinea = miForm.cleaned_data.get("nombreAerolinea")
            paquete.estadiaNoches = miForm.cleaned_data.get("estadiaNoches")
            paquete.save()
            contexto = { "paquetes": Paquetes.objects.all() }
            return render(request, "viajes/paquetes.html", contexto)            
    else:
        miForm = Paquetesform(initial={"hotel": paquete.hotel, "nombreAerolinea": paquete.nombreAerolinea, "estadiaNoches": paquete.estadiaNoches})

    return render(request, "viajes/paquetesForm.html", {"form": miForm})

@login_required
def paquetesDelete(request, id_paquete):
    paquete = Paquetes.objects.get(id=id_paquete)
    paquete.delete()
    contexto = { "paquetes": Paquetes.objects.all() }
    return render(request, "viajes/paquetes.html", contexto)


#___ Vuelos___:

class VueloList(ListView):
    model = Vuelos
#no requiere login
    
class VueloCreate(LoginRequiredMixin, CreateView):
    model = Vuelos
    fields = ["nombreAerolinea"]
    success_url = reverse_lazy("vuelos")
    
class VueloUpdate(LoginRequiredMixin, UpdateView):
    model = Vuelos
    fields = ["nombreAerolinea"]
    success_url = reverse_lazy("vuelos") 

class VueloDelete(LoginRequiredMixin, DeleteView):
    model = Vuelos
    success_url = reverse_lazy("vuelos") 


#_______________________________#
# Login / logout / registration #

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            try: 
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            
            return render(request, "viajes/index.html")
        else:
            return redirect(reverse_lazy('login'))
        
    else:
        miForm = AuthenticationForm()
        
    return render(request, "viajes/login.html", {"form": miForm})
        
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()  
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
        
    return render(request, "viajes/registro.html", {"form": miForm})  

#_______________________________#
# Edición de Perfil / Avatar #

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:             
        miForm = UserEditForm(instance=usuario)  
    
    return render(request, "viajes/editarPerfil.html", {"form": miForm})  
  
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "viajes/cambiarClave.html"
    success_url = reverse_lazy("home")

@login_required    
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home')) 
    else:             
        miForm = AvatarForm()  
    
    return render(request, "viajes/agregarAvatar.html", {"form": miForm})
