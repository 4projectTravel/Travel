from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('map_kamakura', views.map_restaurant, name='map_kamakura'),
   #path('spot_delete',views.spot_delete, name='spot_delete'),
]
