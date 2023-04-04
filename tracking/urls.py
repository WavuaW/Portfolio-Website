from .views import TrackingViews
from django.urls import path

urlpatterns=[
    path('track/<int:tracking_no>/', 
        TrackingViews.as_view()
    ),
    path('track/', TrackingViews.as_view(), 
        name="tracking"
    ),
]