from django.contrib import admin
from .models import Persona


class admPersona(admin.ModelAdmin):
    list_display=["rut","nombre","apellido"]
    list_editable=["nombre","apellido"]
    
    class Meta:
        model=Persona

admin.site.register(Persona, admPersona)
