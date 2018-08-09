from django.db import models

# Create your models here.
class Order (models.Model):
    name = models.CharField(max_length=200);
    phone = models.CharField(max_length=20);
    address = models.TextField();
    email_id = models.EmailField();
    invoice_no = models.CharField(max_length=50, editable=True, blank=True, null= True, default='');
    invoice_date = models.DateField(blank=True, null=True);
    delivery_date = models.DateField(blank=True, null=True);
    product_id = models.TextField();
    payment_option = models.CharField(max_length=50);
    amount = models.IntegerField();
    vat = models.IntegerField();
    order_status = models.CharField(max_length=50);
