from django.shortcuts import render
import xlrd
from models import Films

#A partir du tableau excel creation d'un tableau python pour la base de donnees
base = xlrd.open_workbook('Base_films.xls')
tab = base.sheet_by_name(u'Feuil1')

for i in range(len(tab.col_values(0))):
    Films(titre_original = tab.col_values(0)[i], titre_francais = tab.col_values(1)[i], realisateur = tab.col_values(2)[i], couleur = tab.col_values(3)[i],annee = tab.col_values(4)[i],pays = tab.col_values(5)[i], genre = tab.col_values(6)[i], acteurs = tab.col_values(7)[i], actrices = tab.col_values(8)[i], appreciation = tab.col_values(9)[i], scenario = tab.col_values(10)[i], origine = tab.col_values(11)[i], photographie = tab.col_values(12)[i], musique = tab.col_values(13)[i]).save()
