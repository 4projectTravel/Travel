from django.shortcuts import render, get_object_or_404
#from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from .models import Map
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse # 追加



#class TemplateMapView(TemplateView):
    #template_name = 'map/index.html'
    #model = Map

def index(request):
    template = loader.get_template('map/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def map_restaurant(request):
    template = loader.get_template('map/map_restaurant.html')
    context = {}

    model = Map

    return HttpResponse(template.render(context, request))
