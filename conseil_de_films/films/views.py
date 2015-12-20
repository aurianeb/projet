from django.shortcuts import render
import xlrd
# Create your views here.

#A partir du tableau excel creation d'un tableau python pour la base de donnees
base = xlrd.open_workbook('Base_films.xls')
tab = base.sheet_by_name(u'Feuil1')
titre_original = tab.col_values(0)
titre_francais = tab.col_values(1)
realisateur = tab.col_values(2)
couleur = tab.col_values(3)
annee = tab.col_values(4)
pays = tab.col_values(5)
genre = tab.col_values(6)
acteurs = tab.col_values(7)
actrices = tab.col_values(8)
appreciation = tab.col_values(9)
scenario = tab.col_values(10)
origine = tab.col_values(11)
photographie = tab.col_values(12)
musique = tab.col_values(13)