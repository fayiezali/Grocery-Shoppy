from django.shortcuts import render
from django.contrib import messages
from .models import *

def checkout_DEF(request):
    if request.method == "POST" and request.user.is_authenticated and not request.user.is_anonymous:
        
        
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        phone_number = request.POST['phone_number']
        payment = request.POST['payment']
        
        total_VAR = None 
        order_VAR = OrderMODEL.objects.get(order_user=request.user , order_is_finished=False)
        OrderDetails_VAR = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR)

        for sub in OrderDetails_VAR:
            total_VAR = 0
            total_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity

            shipping_adress = CheckoutDetail_MODEL.objects.create(
                address=address, city=city , 
                phone_number=phone_number , 
                state=state, zipcode=zipcode , 
                user=request.user , 
                total_amount=total_VAR , 
                order=order_VAR , 
                payment=payment)
            shipping_adress.save()
            
            # order_is_finished_VAR = OrderMODEL.objects.all().filter(order_user= request.user ,order_is_finished=False)
        # if OrderMODEL.objects.all().filter(order_user= request.user ,order_is_finished=False):
            # user whose total_amount is to be updated.
            user = request.user

            # get current user instance of balance_data
            order_is_finished_VAR = OrderMODEL.objects.get(order_user=user ,order_is_finished=False)

            # update total_amount by adding amount to its total_amount
            order_is_finished_VAR.order_is_finished = True

            order_is_finished_VAR.save()
            
            context = {
                    'order_VAR':order_VAR,
                    'OrderDetails_VAR':OrderDetails_VAR,
                    'total_VAR':total_VAR,
                    }
            messages.success(request, "A-Order Is Successfully.")
            return render(request, "checkout/checkout.html", context)
        # return render(request, "checkout.html", {'alert':alert, 'id':id})
    messages.info(request    , "B")
    return render(request, "checkout/checkout.html")
    # return render(request, "checkout.html", {'items':items, 'order':order, 'cartItems':cartItems})




def cash_in(request, amount):

    new_amount = request.user.balance_data.total_amount + amount

    balance_data.total_amount = new_amount
    balance_data.save()

    return HttpResponse(request.user.balance_data.total_amount)


def cash_in(request, amount):
    # user whose total_amount is to be updated.
    user = request.user

    # get current user instance of balance_data
    user_current_balance = balance_data.objects.get(user=user)

    # update total_amount by adding amount to its total_amount
    user_current_balance.total_amount = user_current_balance.total_amount + amount

    # save changes to database
    user_current_balance.save()
    return HttpResponse(user_current_balance.total_amount)