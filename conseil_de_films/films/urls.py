
from django.conf.urls import patterns, url

urlpatterns = patterns('films.views',
    url(r'^accueil', 'preference'), #La page de la recherche
    url(r'^data_base/','create_DB'), # Créé la base de données
    url(r'^api/formulaire/','api_formulaire'), 
)