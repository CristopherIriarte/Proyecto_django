from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    consola = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=0)

    def __str__(self):
        return self.titulo