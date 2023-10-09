from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('map_restaurant', views.map_restaurant, name='map_restaurant'),
   path('map_shrine', views.map_shrine, name='map_shrine'),
   #path('spot_delete',views.spot_delete, name='spot_delete'),
]
