from django.urls import path

from . import views

urlpatterns = [
   path('map_kamakura', views.map_kamakura, name='map_kamakura'),
]
