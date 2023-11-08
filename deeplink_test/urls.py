from django.contrib import admin
from django.urls import path

from landing.views import landing, well_known, pokemons

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing, name='landing'),
    path('pokemons/', pokemons, name='pokemons'),
    path('.well-known/assetlinks.json', well_known, name='well-known')
]
