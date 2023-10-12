from django.urls import path, include

from . import views
#gmapに関する追記
#from gmap.models import Spot
#from rest_framework import routers, serializers, viewsets
urlpatterns = [
    #path('', views.index_view, name='index'),
    path('gmap/', views.TemplateGmapView.as_view()),
    #gmapに関する追記
    #path('gmap/api/', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
