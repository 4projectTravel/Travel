from django.urls import path

from . import views

urlpatterns = [
   path('kamakura/', views.map_kamakura, name='map_kamakura'),
]
