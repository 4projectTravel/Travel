from django.urls import path

from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('map_restaurant', views.map_restaurant, name='map_restaurant'),
   #path('spot_delete',views.spot_delete, name='spot_delete'),
]
