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
    #Redirige vers la page html choix à l'appel de /films/accueil
        
    return render(request, 'films/choix.html', locals())



@api_view(['GET', 'POST'])
def api_formulaire(request):

    #On acquérit les préférences de l'internaute
    params = request.GET
    Films_possibles=[]
    deja_vu=int(params['deja_vu'])
    
    #On filtre les films ne répondant pas aux critères
    Liste_filtree_1 = Films.objects.filter(pays__contains=params['choix_pays'], genre__contains=params['choix_genre'], couleur__contains=params['choix_couleur'], annee__range=(params['choix_datemin'],params['choix_datemax']))
    for film in Liste_filtree_1:
      if (params['choix_act1'] in str(film.acteurs) or params['choix_act1'] in str(film.actrices)):
          Films_possibles.append([film.titre_original,
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

    #Si aucun film ne correspond
    if len(Films_possibles)==0 :
        resp={
            "data":Films_possibles,
            "msg1": "Désolé mais nous n'avons pas trouvé de film correspondant à vos critères",
            "msg2":"",
            "titre_original":"",         
            "titre_francais":"",
            "realisateur":"",
            "deja_vu":deja_vu
        }
    #Si les films correspondant ont déjà tous été proposés
    elif deja_vu >= len(Films_possibles):
        resp={
            "data":Films_possibles,
            "msg1": "Désolé mais nous n'avons pas d'autre film à vous proposer",
            "msg2":"",
            "titre_original":"",         
            "titre_francais":"",
            "realisateur":"",
            "deja_vu":deja_vu
        }

    #S'il reste des films à proposer
    else :

        resp={
            "data":Films_possibles,
            "msg1":"Le film proposé est : ",
            "msg2":" de ",
            "titre_original":Films_possibles[deja_vu][0],         
            "titre_francais":Films_possibles[deja_vu][1],
            "realisateur":Films_possibles[deja_vu][2],
            "deja_vu":deja_vu+1
        }
    return Response(resp)
