from django.urls import path

from . import views

urlpatterns = [
     path('spot/', views.AddressList.as_view(), name='address_list'),
     path('spot/genre/', views.GenreList.as_view() ,name='genre_list'),

     #path('spot/genre/', (views.AddressList.as_view() and views.GenreList.as_view()), name='genre_list'),
]
