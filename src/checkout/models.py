from django.db import models
from orders.models import *
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now


class CheckoutDetail_MODEL(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(OrderMODEL, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True,null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    payment = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(default=now)

    def __str__(self):
        return self.address
