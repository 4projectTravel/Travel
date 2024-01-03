from django.contrib import admin
from .models import Post3 , Review3, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class Post3Resource(resources.ModelResource):
    class Meta:
        model = Post3

class Post3Admin(ImportExportModelAdmin):
    resource_class = Post3Resource

class Review3Resource(resources.ModelResource):
    class Meta:
        model = Review3

class Review3Admin(ImportExportModelAdmin):
    resource_class = Review3Resource

admin.site.register(Post3, Post3Admin)
admin.site.register(Review3, Review3Admin)
admin.site.register(Category)
