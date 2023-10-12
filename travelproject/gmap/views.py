from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from .models import Gmap
from rest_framework import routers, serializers, viewsets


class TemplateGmapView(TemplateView):
    template_name = 'gmap/index.html'
    model = Gmap

class SpotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spot
        fields = ('name', 'address', 'lat', 'lng')

class SpotViewSet(viewsets.ModelViewSet):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer




router = routers.DefaultRouter()
router.register(r'spot', SpotViewSet)
