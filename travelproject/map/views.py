from django.shortcuts import render
#from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from .models import Map

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
    return HttpResponse(template.render(context, request))

def map_shrine(request):
    template = loader.get_template('map/map_shrine.html')
    context = {}
    return HttpResponse(template.render(context, request))
