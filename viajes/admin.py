from django.contrib import admin

# Register your models here.
from .models import *

class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ("hotel", "categoriaEstrellas")
    list_filter = ("hotel",)

admin.site.register(Alojamientos, AlojamientoAdmin)
admin.site.register(Paquetes)
admin.site.register(Vuelos)