from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.lista_videojuegos, name='lista_videojuegos'),
    path('crear/', views.crear_videojuego, name='crear_videojuego'),
    path('editar/<int:videojuego_id>/', views.editar_videojuego, name='editar_videojuego'),
    path('eliminar/<int:videojuego_id>/', views.eliminar_videojuego, name='eliminar_videojuego'),
]