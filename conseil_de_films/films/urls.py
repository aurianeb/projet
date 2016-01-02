# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:42:26 2015

@author: Margot
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('films.views',
    url(r'^accueil', 'preference'),
    url(r'^data_base/','create_DB'), # ne faire qu'une fois au début (je l'ai fait!
    url(r'^api/formulaire/','api_formulaire'),
)