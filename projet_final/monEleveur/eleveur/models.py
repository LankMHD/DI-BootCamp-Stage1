from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime, date


# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=50)
    Adresse = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=50)

class Eleveur(models.Model):
    nom_eleveur = models.CharField(max_length=100)
    Adresse = models.CharField(max_length=100)
    Telephone = models.CharField(max_length=50)

class Formation(models.Model):
    Titre = models.CharField(max_length=250)
    Date = models.DateField(max_length=100)
    Lieu = models.CharField(max_length=50)
    Commentaire = models.CharField(max_length=255)

