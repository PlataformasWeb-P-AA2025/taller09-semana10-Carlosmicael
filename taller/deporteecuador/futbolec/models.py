from django.db import models

# Create your models here.
from django.db import models

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    username_twitter = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=30)
    numero_camiseta = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.equipo.nombre}"

class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.auspiciante})"

class CampeonatoEquipos(models.Model):
    anio = models.IntegerField()
    equipo = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.anio} - {self.equipo.nombre} - {self.campeonato.nombre}"
