from django.db import models
from .models import *
from decimal import Decimal
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now


# Model Proudect
class ProductMODEL(models.Model):
    product_name         = models.CharField(max_length=200)
    product_description  = models.TextField()
    product_price        = models.DecimalField(max_digits=10,decimal_places=2)
    # product_price        = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('00.00'), blank=True , null=True , verbose_name="Price")
    product_image        = models.ImageField(upload_to="Productes_File_Photo/%Y/%m/%d/")
    product_is_active 	 = models.BooleanField(default=False)
    product_publish_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering            = ('-product_publish_date',)
        verbose_name        = "Product"
        verbose_name_plural = "Products" 

    # 'admin'display the field name on a page
    def __str__(self):
        return self.product_name
#
#
#
class OrderMODEL(models.Model):
    order_user        = models.ForeignKey(User , on_delete = models.CASCADE)
    order_order_date  = models.DateTimeField(auto_now_add=True)
    order_details     = models.ManyToManyField(ProductMODEL , through='OrderDetailsMODEL')
    order_is_finished = models.BooleanField(default=False)
    class Meta:
        ordering = ('-order_order_date',)
        verbose_name = "Order"
        verbose_name_plural = "Orders" 

    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'User Name: ' + self.order_user.username + '-' \
                'Order Id: ' + str(self.id) 
#
#
#
class OrderDetailsMODEL(models.Model):
    OrderDetails_product  = models.ForeignKey(ProductMODEL , on_delete = models.CASCADE)
    OrderDetails_order    = models.ForeignKey(OrderMODEL   , on_delete = models.CASCADE)
    OrderDetails_price    = models.DecimalField(max_digits=10,decimal_places=2)
    OrderDetails_quantity = models.IntegerField()
    class Meta:
        ordering = ('-OrderDetails_order',)
        verbose_name = "Order Detail"
        verbose_name_plural = "Order Details" 

    # 'admin'display the field name on a page
    # \: write code of more than 1 line in the Python interpreter
    def __str__(self):
        return  'User Name : ' + str(self.OrderDetails_order.order_user) + ' - ' +\
                'Product: ' + self.OrderDetails_product.product_name + ' - ' +\
                'Order Id: ' + str(self.OrderDetails_order.id)
