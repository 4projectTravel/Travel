from django.urls import path
from .apps import AppConfig as config

from . import views



urlpatterns = [
   path('itinerary/list/', views.ListItineraryView.as_view(), name='list-itinerary'),
   path('mypage_top/', views.ListItineraryNewView.as_view(), name='mypage_top'),
   path('itinerary/list_record/', views.ListItineraryRecordView.as_view(), name='list-itinerary-record'),
   path('itinerary/list_all/', views.ListItineraryAllView.as_view(), name='list-itinerary-all'),
   path('itinerary/kamakura_list_all/', views.ListKamakuraItineraryAllView.as_view(), name='list-kamakura-itinerary-all'),
   path('itinerary/<int:pk>/detail/', views.DetailItineraryView.as_view(), name='detail-itinerary'),
   path('itinerary/<int:pk>/detail_all/', views.DetailItineraryAllView.as_view(), name='detail-itinerary-all'),
   path('itinerary/create/', views.CreateItineraryView.as_view(), name='create-itinerary'),
   #path('itinerary/create/', views.CreateItineraryView, name='create-itinerary'),
   path('itinerary/<int:pk>/update/', views.UpdateItineraryView.as_view(), name='update-itinerary'),
   #path('itinerary/<int:pk>/review/update/', views.UpdateReviewView.as_view(), name='update-review'),
   path('itinerary/<int:itinerary_id>/review/', views.CreateReviewView.as_view(), name='review-itinerary'),
   path('itinerary/<int:pk>/delete/', views.DeleteItineraryView.as_view(), name='delete-itinerary'),
]
