from django.urls import path
from authentication import views

urlpatterns = [
    path('shipments/', views.ShipmentListView.as_view()),
    path('shipments/<int:pk>/', views.ShipmentDetailView.as_view()),
]