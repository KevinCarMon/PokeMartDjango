from django.shortcuts import redirect, render
from PokeMartApp.models import PokeMart
from PokeMartApp.forms import FormPokeMart

# Create your views here.
#Pagina Principal del Index

#Bien
def index(request):
    return render(request, 'PokeMartApp/index.html')

def listadoProductos(request):
    productos = PokeMart.objects.all()
    data = {'productos': productos}
    return render(request, 'PokeMartApp/listadoProductos.html', data)

#Bien
def agregarProducto(request):
    form = FormPokeMart()
    if request.method == 'POST':
        form = FormPokeMart(request.POST)
        if form.is_valid():
            form.save()
        return index(request)

    data = {'form': form}
    return render(request, 'PokeMartApp/agregarProductos.html', data)


#Bien
def eliminarProducto(request, id):
    productos = PokeMart.objects.get(id=id)
    productos.delete()
    return listadoProductos(request)
#Bien
def actualizarProducto(request, id):
    productos = PokeMart.objects.get(id = id)
    form = FormPokeMart(instance=productos)
    if request.method == 'POST':
        form = FormPokeMart(request.POST, instance=productos)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'PokeMartApp/agregarProductos.html', data)


