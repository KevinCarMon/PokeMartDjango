from django import forms
from PokeMartApp.models import PokeMart
from django.forms import ModelForm

class FormPokeMart(forms.ModelForm):
    nombreObjeto = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=100000)
    cantidad = forms.IntegerField(min_value=1, max_value=100000)
    lugar = forms.CharField(min_length=3, max_length=50)
    tipo = forms.CharField(min_length=3, max_length=50)
    fechaCompra = forms.DateField()
    class Meta:
        model = PokeMart
        fields = '__all__'


