from django.db import models

# Create your models here.

class Mitarbeiter(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gehalt = models.DecimalField(max_digits=10, decimal_places=2)
    schichtzeiten = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Artikel(models.Model):
    id = models.AutoField(primary_key=True)
    artikelnummer = models.IntegerField(max_length=50)
    beschreibung = models.CharField(max_length=255)
    lagerbestand = models.IntegerField(max_length=50)

    def __str__(self):
        return f"{self.artikelnummer} {self.beschreibung}"


class Pferd(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    gewicht = models.FloatField()
    herkunft = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
