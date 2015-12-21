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

#Supprimer une ligne dans le tableau
def supprimer_ligne(i) :
    del(titre_original[i])
    del(titre_francais[i])
    del(realisateur[i])
    del(couleur[i])
    del(annee[i])
    del(pays[i])
    del(genre[i])
    del(acteurs[i])
    del(actrices[i])
    del(appreciation[i])
    del(scenario[i])
    del(origine[i])
    del(photographie[i])
    del(musique[i])
   
#Fonction qui permet de garder uniquement les films d'un certain type (ex : fantastique)
def selection(categorie, choix) : # ex : categorie = genre, choix = western
    for i in range(len(categorie)-1,0,-1) :
        if categorie[i] != choix :
            supprimer_ligne(i)
 
#exemple de qql qui n'aime que les films US           
selection(pays, 'USA') #Attention dans le tableau souvent c'est " USA" donc il faut enlever l'espace pour que ça marche
#Attention dans le tableau souvent c'est " USA" donc il faut enlever l'espace pour que ça marche