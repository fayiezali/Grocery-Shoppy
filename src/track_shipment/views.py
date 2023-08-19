from django.shortcuts import render, redirect
from .models import *
from orders. models import *
from track_shipment. models import *
from django.contrib import messages
from django.contrib.auth.models import User
#
#
#
def track_shipment_DEF(request):
    # if not request.user.is_authenticated:
    #     return redirect('login-URL')
    if request.method == "POST":
        order_id = request.POST['order_id']
        order = OrderMODEL.objects.filter(id=order_id).first()
        order_items = OrderDetailsMODEL.objects.filter(OrderDetails_order=order)
        update_order = UpdateOrder_MODEL.objects.filter(order_id=order_id)
        # print(update_order)
        shipment_track_VAR = ShipmentTrackMODEL.objects.filter(shipment_track_order_id=order_id)
        messages.success(request, 'OK-01')
        return render(request, "track_shipment/track_shipment.html", {'order_items':order_items, 'update_order':update_order,'shipment_track_VAR':shipment_track_VAR })
    return render(request, "track_shipment/track_shipment.html")

 