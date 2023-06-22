from django.shortcuts import render, redirect
from .models import Videojuego
from .forms import VideojuegoForm

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'juegos/lista_videojuegos.html', {'videojuegos': videojuegos})

def crear_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'juegos/crear_videojuego.html', {'form': form})

def editar_videojuego(request, videojuego_id):
    videojuego = Videojuego.objects.get(id=videojuego_id)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'juegos/editar_videojuego.html', {'form': form, 'videojuego': videojuego})

def eliminar_videojuego(request, videojuego_id):
    videojuego = Videojuego.objects.get(id=videojuego_id)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('lista_videojuegos')
    return render(request, 'juegos/eliminar_videojuego.html', {'videojuego': videojuego})