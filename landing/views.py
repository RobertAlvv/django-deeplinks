from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html', {})

def pokemons(request):
    return render(request, 'pokemons.html', {})


def well_known(request):
    return render(request, 'assetlinks.json', {}, content_type='application/json')
