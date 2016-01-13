#-*- coding: utf-8 -*-
from django.shortcuts import render
import xlrd
from films.models import Films


from random import *
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

def create_DB(request):
    
    #A partir du tableau excel creation d'un tableau python pour la base de donnees
    base = xlrd.open_workbook('films/Base_films.xls')
    tab = base.sheet_by_name(u'Feuil1')
    for i in range(1,2855): #fin du tableau à 2855
        nouveau_film = Films(titre_original=tab.col_values(0)[i], 
                             titre_francais=tab.col_values(1)[i],
                             realisateur=tab.col_values(2)[i],
                             couleur=tab.col_values(3)[i],
                             annee=tab.col_values(4)[i],
                             pays=tab.col_values(5)[i], 
                             genre=tab.col_values(6)[i], 
                             acteurs=tab.col_values(7)[i], 
                             actrices=tab.col_values(8)[i], 
                             appreciation=tab.col_values(9)[i], 
                             scenario=tab.col_values(10)[i], 
                             provenance=tab.col_values(11)[i], 
                             photographie=tab.col_values(12)[i], 
                             musique=tab.col_values(13)[i])
        nouveau_film.save()
        
    return render(request, 'films/data_base.html')


def preference(request):
        
    return render(request, 'films/choix.html', locals())

@api_view(['GET', 'POST'])
def api_formulaire(request):
    params = request.GET
    L=[]
    
    ma_liste = Films.objects.filter(pays__contains=params['choix_pays'], genre__contains=params['choix_genre'], couleur__contains=params['choix_couleur'], annee__range=(params['choix_datemin'],params['choix_datemax']))
    for film in ma_liste:
      if (params['choix_act1'] in str(film.acteurs) or params['choix_act1'] in str(film.actrices)):
          L.append([film.titre_original,
                    film.titre_francais,
                    film.realisateur,
                    film.couleur,
                    str(film.annee),
                    film.pays,
                    film.genre,
                    film.acteurs,
                    film.actrices,
                    film.appreciation,
                    film.scenario,
                    film.provenance,
                    film.photographie,
                    film.musique])
                  
    random=randint(0,len(L)-1)

    resp={
            "data":L  ,          
            "titre_francais":L[random][1],
            "realisateur":L[random][2]
    
    }
    return Response(resp)
