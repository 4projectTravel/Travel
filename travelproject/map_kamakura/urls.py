from django.urls import path

from . import views

app_name = 'map_kamakura'
urlpatterns = [
   path('', views.map, name='map'),
]
