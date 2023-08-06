from django.shortcuts import render , redirect
from django.contrib import messages
from . models import *
from django.utils import timezone


def add_to_cart_DEF_(request):
    if 'pro_id' in request.GET and 'qty' in request.GET and  request.user.is_authenticated and not request.user.is_anonymous:
        pro_id = request.GET['pro_id']
        qty    = request.GET['qty']
        
        order = OrderMODEL.objects.all().filter(order_user=request.user , 
            order_is_finished=False)
        if not ProductMODEL.objects.all().filter(id=pro_id).exists():
            return redirect("dashboard-URL")
        pro = ProductMODEL.objects.get(id=pro_id)
        
        if order:
            messages.success(request    , "There is an Old Request.")
            old_order = OrderMODEL.objects.get(order_user=request.user , 
            order_is_finished=False)
            orderdetails = OrderDetailsMODEL.objects.create(OrderDetails_product=pro , OrderDetails_order = old_order , OrderDetails_price=pro.product_price , OrderDetails_quantity=qty)
            messages.success(request    , "Was Added To Cart For Old Order.")
        else:
            messages.success(request    , "This Is New Order.")
            new_order = OrderMODEL()
            new_order.order_user = request.user
            new_order.order_order_date = timezone.now()
            new_order.order_is_finished = False
            new_order.save()
            orderdetails = OrderDetailsMODEL.objects.create(OrderDetails_product=pro , OrderDetails_order=new_order , OrderDetails_price=pro.product_price , OrderDetails_quantity=qty)
            messages.success(request    , "Was Added To Cart For Old Order.")
        # return redirect("dashboard-URL" + request.GET['pro_id'])
        return redirect("dashboard-URL")

    else:
        return redirect("dashboard-URL")

def add_to_cart_DEF(request):
    if 'pro_id' in request.GET and 'qty' in request.GET and  request.user.is_authenticated and not request.user.is_anonymous:
        pro_id_VAR = request.GET['pro_id']
        qty_VAR    = request.GET['qty']
        
        order_VAR = OrderMODEL.objects.all().filter(order_user=request.user , 
            order_is_finished=False)
        if not ProductMODEL.objects.all().filter(id=pro_id_VAR).exists():
            return redirect("dashboard-URL")
        pro_VAR = ProductMODEL.objects.get(id=pro_id_VAR)
        
        if order_VAR:
            messages.success(request    , "There is an Old Request.")
            old_order_VAR = OrderMODEL.objects.get(order_user=request.user , 
            order_is_finished=False)
            orderdetails_VAR = OrderDetailsMODEL.objects.create(OrderDetails_product=pro_VAR , OrderDetails_order = old_order_VAR , OrderDetails_price=pro_VAR.product_price , OrderDetails_quantity=qty_VAR)
            messages.success(request    , "Was Added To Cart For Old Order.")
        else:
            messages.success(request    , "This Is New Order.")
            new_order_VAR = OrderMODEL()
            new_order_VAR.order_user = request.user
            new_order_VAR.order_order_date = timezone.now()
            new_order_VAR.order_is_finished = False
            new_order_VAR.save()
            orderdetails = OrderDetailsMODEL.objects.create(OrderDetails_product=pro_VAR , OrderDetails_order=new_order_VAR , OrderDetails_price=pro_VAR.product_price , OrderDetails_quantity=qty_VAR)
            messages.success(request    , "Was Added To Cart For New Order.")
        # return redirect("dashboard-URL" + request.GET['pro_id'])
        return redirect("dashboard-URL")

    else:
        return redirect("dashboard-URL")


def cart_DEF(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        if OrderMODEL.objects.all().filter(order_user= request.user ,
            order_is_finished=False):
            order_VAR = OrderMODEL.objects.get(order_user=request.user , 
            order_is_finished=False)
            OrderDetails_VAR = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR)
            total_VAR = 0
            for sub in OrderDetails_VAR:
                total_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity
            context = {
                'order_VAR':order_VAR,
                'OrderDetails_VAR':OrderDetails_VAR,
                'total_VAR':total_VAR,
            }
    return render (request , 'orders/cart.html' ,  context) 