# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 13:42:26 2015

@author: Margot
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('films.views',
    url(r'^accueil', 'recuperation_donnes'),
)