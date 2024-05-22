from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count, Avg
from django.db.models import F
from django.utils import timezone
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=257)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50,unique=True,primary_key=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50,unique=True,primary_key=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformanceModel(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender,instance,**kwargs):
    if instance.status == 'completed' and instance.delivered_data is None:
        instance.delivered_data = timezone.now()
        instance.save()

    complete_order = PurchaseOrder.objects.filter(vendor=instance.vendor,status='completed')

    on_time_deliveries = complete_order.filter(delivery_date__gte=F('delivered_data'))
    on_time_delivery_rate = on_time_deliveries.count() / complete_order.count()
    instance.vendor.on_time_delivery_rate = on_time_delivery_rate if on_time_delivery_rate else 0

    complete_order_with_rating = complete_order.exclude(quality_rating__isnull=True)
    quality_rating_avg = complete_order_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
    instance.vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg else 0
    instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_response_time(sender,instance,**kwargs):
    response_time = PurchaseOrder.objects.filter(vendor=instance.vendor,acknowledgement_date__isnull=False).value_list('acknowledgement_date','issue_date')
    average_reponse_time = sum((ack_date - issue_date).total_seconds()for ack_date, issue_date in response_time)
    if average_reponse_time < 0:
        average_reponse_time = 0
    if response_time:
        average_reponse_time = average_reponse_time / len(response_time)
    else:
        average_reponse_time = 0
    instance.vendor.average_response_time = average_reponse_time
    instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender,instance,**kwargs):
    fulfillment_order = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
    fulfillment_rate = fulfillment_order.count() / PurchaseOrder.objects.filter(vendor=instance.vendor).count()
    instance.vendor.fulfillment_rate = fulfillment_rate
    instance.vendor.save()