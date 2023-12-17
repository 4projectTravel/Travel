from django.urls import path

from . import views

app_name = 'map_all'
urlpatterns = [
   path('kamakura/', views.kamakura, name='kamakura'),
   path('sapporo/', views.sapporo, name='sapporo'),
   path('', views.sapporo, name='sapporo'),
]
