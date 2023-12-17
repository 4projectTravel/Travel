from django.urls import path

from . import views



urlpatterns = [

    path('topA', views.topA, name='topA'),
    path('post2/', views.ListPost2View.as_view(), name='list-post2'),
    path('post/likepost/', views.ListLikePostView.as_view(), name='list-likepost'),
    path('post2/<int:pk>/detail/', views.DetailPost2View.as_view(),
name='detail-post2'),
    path('post2/create/', views.CreatePost2View.as_view(), name='create-post2'),
    path('post2/<int:post2_id>/review/', views.CreateReview2View.as_view(),
name='review-post2'),
    path('postlike2/', views.postlike2, name='postlike2'),  # 追加
    path('like/', views.like, name='like'),  # 追加
    path('itinerary/', views.move_to_itinerary, name='move_to_itinerary'),
    path('travelling/', views.move_to_traveling, name='move_to_traveling'),
]
