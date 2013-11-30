from django.forms import ModelForm
from django import forms
from recicladora.apps.app_recicladora.models import *

class rutaForm(ModelForm):
    class Meta:
        model = ruta

class aseguradoraForm(ModelForm):
    class Meta:
        model = aseguradora

class camion_aseguradoraForm(ModelForm):
    class Meta:
        model = camion_aseguradora
        
        
class alta_empleadoForm(ModelForm):
    class Meta:
        model = trabajador

class alta_camionForm(ModelForm):
    class Meta:
        model = camion