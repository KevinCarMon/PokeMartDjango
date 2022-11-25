from django.contrib import admin
from PokeMartApp.models import PokeMart

# Register your models here.
class PokeMartAdmin(admin.ModelAdmin):
    list_display = ('nombreObjeto', 'precio', 'cantidad', 'lugar', 'tipo', 'fechaCompra')
admin.site.register(PokeMart)