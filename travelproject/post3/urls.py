from django.urls import path

from . import views



urlpatterns = [

    path('topA', views.topA, name='topA'),
    path('post3/', views.ListPost3View.as_view(), name='list-post3'),
    path('post3/likepost/', views.ListLikePostView.as_view(), name='list-likepost3'),
    path('post3/<int:pk>/detail/', views.Detailpost3View.as_view(),
name='detail-post3'),
    path('post3/create/', views.Createpost3View.as_view(), name='create-post3'),
    path('post3/<int:post3_id>/review/', views.CreateReview3View.as_view(),
name='review-post3'),
    path('postlike3/', views.postlike3, name='postlike3'),  # 追加
    path('like/', views.like, name='like'),  # 追加
    path('itinerary/', views.move_to_itinerary, name='move_to_itinerary'),
    path('travelling/', views.move_to_traveling, name='move_to_traveling'),
]
