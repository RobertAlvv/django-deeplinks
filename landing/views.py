from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html', {})


def well_known(request):
    return render(request, 'assetlinks.json', {})
