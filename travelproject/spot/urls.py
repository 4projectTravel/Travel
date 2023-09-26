from django.urls import path
from . import views

app_name = 'spot'

urlpatterns = [
    path('spot/', views.AddressGenreList.as_view(), name='addressgenre_list'), #追加
]
