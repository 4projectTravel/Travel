from django.urls import path

from . import views



urlpatterns = [

    path('topA', views.topA, name='topA'),
    #path('topB', views.topB, name='topB'),
    #path('selection/', views.selection, name='selection'),
    #path('post/', views.index_view, name='index'),
    path('post/', views.ListPostView.as_view(), name='list-post'),
    path('post/likepost/', views.ListLikePostView.as_view(), name='list-likepost'),
    path('post/<int:pk>/detail/', views.DetailPostView.as_view(),
name='detail-post'),
    path('post/create/', views.CreatePostView.as_view(), name='create-post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(),
name='delete-post'),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(),
name='update-post'),
    path('post/<int:post_id>/review/', views.CreateReviewView.as_view(),
name='review-post'),
    path('postlike/', views.postlike, name='postlike'),  # 追加
    path('like/', views.like, name='like'),  # 追加
    path('itinerary/', views.move_to_itinerary, name='move_to_itinerary'),
    path('travelling/', views.move_to_traveling, name='move_to_traveling'),
    #path('', views.logout_view, name='logout'),
    #path('login/', views.logoin_view, name='login'),
    path('map_kamakura/', views.map_restaurant, name='map_kamakura'),

]
