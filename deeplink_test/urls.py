from django.contrib import admin
from django.urls import path

from landing.views import landing, well_known

urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', landing, name='landing'),
    path('.well-known/assetlinks.json', well_known, name='well-known')
]
