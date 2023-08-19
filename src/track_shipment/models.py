from django.db import models
from .models import *
from orders.models import *

from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now

class ShipmentTrackMODEL(models.Model):
    shipment_track_user              = models.ForeignKey(User , on_delete = models.CASCADE)
    shipment_track_order_id          = models.ForeignKey(OrderMODEL, on_delete=models.CASCADE)
    shipment_track_confirmed_order   = models.BooleanField(default=False)
    shipment_track_Processing_order  = models.BooleanField(default=False)
    shipment_track_dispatch_product  = models.BooleanField(default=False)
    shipment_track_delivery          = models.BooleanField(default=False)
    shipment_track_Product_delivered = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-shipment_track_order_id',)
        verbose_name = "Shipment Track"
        verbose_name_plural = "Shipment Tracs" 

    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'User Name: ' + self.shipment_track_user.username + '-' \
                'Order ID: ' + str(self.shipment_track_order_id) 
#
