from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from .serializers import *
from rest_framework import generics, status
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
# Create your views here.

class VendorListCreateView(generics.ListCreateAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveDestroyAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveDestroyAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = VendorSerializer

class VendorPerformanceView(generics.RetrieveAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)

        return Response({'on_time_delivery_rate' : serializers.data['on_time_delivery_rate'],
                         'quality_rating' : serializers.data['quality_rating'],
                         'average_response_time': serializers.data['average_response_time'],
                         'fulfillment_rate' : serializers.data['fulfillment_rate']})

class AcknowledgementPurchaseOrderView(generics.UpdateAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgement_date = request.data.get('acknowledgement_date')  #timezone.now()
        instance.save()
        response_time = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgement_date__isnull=False).value_list('acknowledgement_date','issue_date')
        average_response_time = sum(abs((ack_date - issue_date).total_seconds()) for ack_date, issue_date in response_time)
        if response_time:
            average_response_time = average_response_time / len(response_time)
        else:
            average_response_time = 0
        instance.vendor.average_response_time = average_response_time
        instance.vendor.save()
        return Response({'acknowledgement_date': instance.acknowledgement_date})