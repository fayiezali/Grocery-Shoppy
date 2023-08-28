from django.db import models
from .models import *
from orders.models import *
from django.contrib.auth.models import User # إستيراد اسم المستخدم


class Tax_MODEL(models.Model):
    """Django Model for State"""
    tax                = models.PositiveIntegerField(default=15 , blank=True , null=True , verbose_name="Tax %")
    divide_one_hundred = models.PositiveIntegerField(default=100 , blank=True , null=True , verbose_name="100")
    
    class Meta:
        ordering            = ('-tax',)
        verbose_name        = "Tax"
        verbose_name_plural = "Taxs" 

    # 'admin'display the field name on a page
    def __str__(self):
        return str(self.tax)
#
#
#

    # tax              = models.CharField(max_length=30 , help_text="Enter Tax", verbose_name="Tax1 %")
    # tax_tax          = models.PositiveIntegerField(default=0,blank=True,null=True, verbose_name="tax_tax2 %")
    # tax_price        = models.DecimalField(default=Decimal(0) ,decimal_places=2, max_digits=10)


# class Product(models.Model):
#     name = models.Charfield(max_lenght=50)
#     price = models.DecimalField(decimal_places=2, max_digits=10)
#     tax = models.PositiveIntegerField()
#     tax_accountant = models.ForeignKey(
#         UserModel,
#         on_delete=models.SET_NULL,
#         related_name='user_tax_accountant',
#         null=True,
#         blank=True
#     )



# class Product(models.Model):
#     name = models.Charfield(max_lenght=50)
#     price = models.DecimalField(decimal_places=2, max_digits=10)
#     tax = models.PositiveIntegerField()



# class Cart(models.Model):
#     items = models.ManyToManyField(ProductMODEL, through="CartProduct")

#     def total(self):
#         total = 0.0
#         for item in self.items.all():
#             total += (item.product.prodPrice * item.quantity)
#         return total



# class Store(models.Model):
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     name = models.CharField(max_length=128, blank=True, default="", verbose_name="Name")



# class StoreAnalytics(models.Model):
#     store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, related_name="store_id")
#     sales_sum = models.DecimalField(
#         max_digits=10, decimal_places=2, default=Decimal(0), verbose_name="Sales")
#     tax = models.IntegerField(
#         default=6, validators=[MaxValueValidator(20), MinValueValidator(0)], verbose_name="Tax %"
#     )