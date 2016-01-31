
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^films/', include('films.urls')),
    url(r'^admin/', include(admin.site.urls)), # La section admin permet notament de gérer facilement à la main la base de données
]
