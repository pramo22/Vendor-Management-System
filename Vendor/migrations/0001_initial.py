# Generated by Django 3.2.9 on 2024-05-17 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('name', models.CharField(max_length=257)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vendor_code', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('on_time_delivery_rate', models.FloatField(default=0)),
                ('quality_rating', models.FloatField(default=0)),
                ('average_response_time', models.FloatField(default=0)),
                ('fulfillment_rate', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('po_number', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(max_length=20)),
                ('quality_rating', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgement_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vendor.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPerformanceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vendor.vendor')),
            ],
        ),
    ]
