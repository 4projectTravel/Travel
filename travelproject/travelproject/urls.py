from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

#map追加ここから
from map.models import Map
from rest_framework import routers, serializers, viewsets


class MapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Map
        fields = ('name', 'address', 'lat', 'lng', 'genre', 'ranking', 'number', 'comment')
class MapViewSet(viewsets.ModelViewSet):
    #queryset = Map.objects.all()
    queryset = Map.objects.order_by('ranking') #ランキング順に並び替える
    serializer_class = MapSerializer

router = routers.DefaultRouter()
router.register(r'map', MapViewSet)
#ここまで



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('post.urls')),
    path('', include('itinerary.urls')),
    path('', include('spot.urls')),
    path('map/', include('map.urls')),
    #map追加ここから
    path('map/api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #ここまで
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
