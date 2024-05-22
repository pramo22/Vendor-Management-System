from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/',VendorListCreateView.as_view(),name='vendor-list-create'),
    path('vendors/<int:pk>',VendorRetrieveUpdateDeleteView.as_view(),name='vendor-retrieve-update-delete'),
    path('purchase-order/',PurchaseOrderListCreateView.as_view(),name='purchase-order-list-create-view'),
    path('purchase-order/<int:pk>/',PurchaseOrderRetrieveUpdateDeleteView.as_view(),name='retrieve-update-delete'),
    path('vendors/<int:pk>/performance/',VendorPerformanceView.as_view(),name='vendor-performance'),
    path('purchase-order/<int:pk>/acknowledgement/',AcknowledgementPurchaseOrderView.as_view(),name='purchase-order-acknowledge'),
]