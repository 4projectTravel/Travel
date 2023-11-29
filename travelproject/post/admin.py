from django.contrib import admin
from .models import Post , Review , Category
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin):
    resource_class = PostResource

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review

class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource

admin.site.register(Post, PostAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)
