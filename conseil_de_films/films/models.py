from django.db import models

# Create your models here.
class Films(models.Model):
    titre_original = models.CharField(max_length=100)
    titre_francais = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    couleur = models.CharField(max_length=100)
    annee = models.IntegerField()
    pays = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    acteurs = models.CharField(max_length=1000)
    actrices = models.CharField(max_length=1000)
    appreciation = models.CharField(max_length=100)
    scenario = models.CharField(max_length=100)
   # provenance = models.CharField(max_length=200)
    photographie = models.CharField(max_length=100)
    musique = models.CharField(max_length=100)