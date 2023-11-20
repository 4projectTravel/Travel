from django.contrib import admin
from .models import Post , Review , Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource

admin.site.register(Post, PostAdmin)
admin.site.register(Review)
admin.site.register(Category)
