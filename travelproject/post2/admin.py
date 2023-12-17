from django.contrib import admin
from .models import Post2 , Review2, Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class Post2Resource(resources.ModelResource):
    class Meta:
        model = Post2

class Post2Admin(ImportExportModelAdmin):
    resource_class = Post2Resource

class Review2Resource(resources.ModelResource):
    class Meta:
        model = Review2

class Review2Admin(ImportExportModelAdmin):
    resource_class = Review2Resource

admin.site.register(Post2, Post2Admin)
admin.site.register(Review2, Review2Admin)
admin.site.register(Category)
