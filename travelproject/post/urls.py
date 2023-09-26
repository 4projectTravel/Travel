from django.urls import path

from . import views

urlpatterns = [

    path('topA', views.topA, name='topA'),
    path('topB', views.topB, name='topB'),
    path('selection/', views.selection, name='selection'),
    path('post/', views.index_view, name='index'),
    path('post/', views.ListPostView.as_view(), name='list-post'),
    path('post/<int:pk>/detail/', views.DetailPostView.as_view(),
name='detail-post'),
    path('post/create/', views.CreatePostView.as_view(), name='create-post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(),
name='delete-post'),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(),
name='update-post'),
    path('post/<int:post_id>/review/', views.CreateReviewView.as_view(),
name='review'),
    path('mypage/', views.move_to_mypage, name='move_to_mypage'),
    path('itinerary/', views.move_to_itinerary, name='move_to_itinerary'),
    path('record/', views.move_to_record, name='move_to_record'),
    path('travelling/', views.move_to_traveling, name='move_to_traveling'),
    #path('', views.logout_view, name='logout'),
    #path('login/', views.logoin_view, name='login'),

    path('map_restaurant/', views.map_restaurant, name='map_restaurant'),
    path('map_leisure/', views.map_leisure, name='map_leisure'),
    path('map_museum/', views.map_museum, name='map_museum'),
    path('map_shrine/', views.map_shrine, name='map_shrine'),
    path('map_hotspring/', views.map_hotspring, name='map_hotspring'),
    path('map_event/', views.map_event, name='map_event'),
]
