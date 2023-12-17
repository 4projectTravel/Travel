from django.urls import path

from . import views

urlpatterns = [
   path('kamakura/', views.map_kamakura, name='map_kamakura'),
   path('sapporo/', views.map_sapporo, name='map_kamakura'),
]
