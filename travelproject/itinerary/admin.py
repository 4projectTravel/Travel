from django.contrib import admin
from .models import Itinerary, Review
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ItineraryResource(resources.ModelResource):
    class Meta:
        model = Itinerary

class ItineraryAdmin(ImportExportModelAdmin):
    resource_class = ItineraryResource


admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(Review)
