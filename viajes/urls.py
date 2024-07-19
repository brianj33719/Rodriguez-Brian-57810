from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca"),
   
    #___ Alojamientos ___:
    path('alojamientos/', alojamientos, name="alojamientos"),
    path('alojamientosForm/', alojamientosform, name="alojamientosForm"),
    path('buscarAlojamientos/', buscarAlojamientos, name="buscarAlojamientos"),
    path('encontrarAlojamientos/', encontrarAlojamientos, name="encontrarAlojamientos"),
    path('alojamientosUpdate/<id_alojamiento>/', alojamientosUpdate, name="alojamientosUpdate"),
    path('alojamientosDelete/<id_alojamiento>/', alojamientosDelete, name="alojamientosDelete"),
    
    #___ Paquetes ___:
    path('paquetes/', paquetes, name="paquetes"),
    path('paquetesForm/', paquetesform, name="paquetesForm"),
    path('paquetesUpdate/<id_paquete>/', paquetesUpdate, name="paquetesUpdate"),
    path('paquetesDelete/<id_paquete>/', paquetesDelete, name="paquetesDelete"),
    
    #___ Vuelos ___:
    path('vuelos/', VueloList.as_view(), name="vuelos"),
    path('vuelosCreate/', VueloCreate.as_view(), name="vuelosCreate"), 
    path('vuelosUpdate/<int:pk>', VueloUpdate.as_view(), name="vuelosUpdate"), 
    path('vuelosDelete/<int:pk>', VueloDelete.as_view(), name="vuelosDelete"),   
    
    #_______________________________#
    
    # Login / logout / registration #
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="viajes/logout.html"), name="logout"),    
    path('registro/', register, name="registro"),
    
    # Edición de perfiles / Avatar #
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
]