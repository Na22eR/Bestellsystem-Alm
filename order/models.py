from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bestellung(models.Model):
    tisch_nr = models.IntegerField()
    uhrzeit = models.DateTimeField(auto_now_add=True)   #auto_now_add: füllt timestamp automatisch bei Erstellen des Objektes aus (editierbar)
    # status = models.IntegerField()
    bedienung = models.ForeignKey(User, on_delete=models.CASCADE)
    gesamtpreis = models.DecimalField(max_digits=7, decimal_places=2)

    def __int__(self):
        return self.tisch_nr


class Speisekarte(models.Model):
    name = models.CharField(max_length=50)
    id_name = models.CharField(max_length=30)
    kategorie = models.IntegerField(blank=True, null=True)
    preis = models.FloatField()
    anzahl = models.IntegerField()
    anzahl_bestellt = models.IntegerField(default=0)
    limit = models.BooleanField()
    verfuegbar = models.BooleanField()

    def __str__(self):
        return self.name


class Bestellposition(models.Model):
    id_bestellung = models.ForeignKey(Bestellung, on_delete=models.CASCADE)
    speise = models.ForeignKey(Speisekarte, on_delete=models.CASCADE)
    preis = models.FloatField()
    anzahl = models.IntegerField()
    anmerkung = models.CharField(max_length=200, blank=True)

    def __int__(self):
        return self.id_bestellung
