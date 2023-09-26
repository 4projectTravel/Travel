from django.contrib import admin
from .models import Genre, Address, GenreCategory, AddressCategory
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre


class GenreAdmin(ImportExportModelAdmin):
    search_fields = ('description',)
    #list_display = ['category_genre','description']
    #list_filter = ('category_genre',)
    list_display = ['category_genre','description']
    list_filter = ('category_genre',)

    resource_class = GenreResource


class GenreCategoryResource(resources.ModelResource):
    class Meta:
        model = GenreCategory


class GenreCategoryAdmin(ImportExportModelAdmin):
    resource_class = GenreCategoryResource


class AddressResource(resources.ModelResource):
    class Meta:
        model = Address


class AddressAdmin(ImportExportModelAdmin):
    search_fields = ('description',)
    #list_display = ['category_address','description']
    #list_filter = ('category_address',)
    list_display = ['category_address','description']
    list_filter = ('category_address',)

    resource_class = AddressResource


class AddressCategoryResource(resources.ModelResource):
    class Meta:
        model = AddressCategory


class AddressCategoryAdmin(ImportExportModelAdmin):
    resource_class = AddressCategoryResource


admin.site.register(GenreCategory, GenreCategoryAdmin)
admin.site.register(AddressCategory, AddressCategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Address, AddressAdmin)
