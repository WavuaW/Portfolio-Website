from django.urls import path
from authentication import views

urlpatterns = [
    path('shipment/', 
         views.ShipmentListView.as_view(), 
         name="shipment",
    ),
    path('shippingto/', 
         views.ShippingToListView.as_view(), 
         name="shippingto"
    ),
    path('shippingfrom/', 
         views.ShippingFromListView.as_view(), 
         name="shippingfrom"
    ),
    path('shipments/<int:pk>/', 
         views.ShipmentDetailView.as_view(), 
         name="shipmets"
    ),
    path('shippingto/<int:pk>/', 
         views.ShippingToDetailView.as_view(), 
         name="shippingto"
    ),
    path('shippingfrom/<int:pk>/', 
         views.ShippingFromDetailView.as_view(), 
         name="shippingfrom"
    ),
  ]