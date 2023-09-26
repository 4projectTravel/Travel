from django.contrib import admin
from .models import AddressCategory, GenreCategory, AddressGenre
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AddressGenreResource(resources.ModelResource):
    class Meta:
        model = AddressGenre


class AddressGenreAdmin(ImportExportModelAdmin):
    search_fields = ('spot',)
    list_display = ['spot','genre','address']
    list_filter = ('genre','address')

    resource_class = AddressGenreResource


class AddressCategoryResource(resources.ModelResource):
    class Meta:
        model = AddressCategory


class AddressCategoryAdmin(ImportExportModelAdmin):
    resource_class = AddressCategoryResource


class GenreCategoryResource(resources.ModelResource):
    class Meta:
        model = GenreCategory


class GenreCategoryAdmin(ImportExportModelAdmin):
    resource_class = GenreCategoryResource

admin.site.register(AddressCategory, AddressCategoryAdmin)
admin.site.register(GenreCategory, GenreCategoryAdmin)
admin.site.register(AddressGenre, AddressGenreAdmin)
