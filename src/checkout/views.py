from django.shortcuts import render
from django.contrib import messages
from .models import *
#
#
#
# # VER:Variables        
def checkout_DEF(request):
        # trying to check Request Method Is POST and if the user is authenticated and not anonymous
    if request.method == "POST" and request.user.is_authenticated and not request.user.is_anonymous:
        # Verify the validity of the entered data
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        phone_number = request.POST['phone_number']
        payment = request.POST['payment']
        # Clear the variable data
        total_VAR = None 
        # select all orders that the user is currently viewing and filter them to only show those that are not yet finished.
        order_VAR = OrderMODEL.objects.get(order_user=request.user , order_is_finished=False)
            #  The code is trying to get the order that is finished.
            #  It does this by getting the OrderMODEL object and then checking if it has an attribute called "is_finished".
            #  If it doesn't have that attribute, then it will set its value to False.
            #  The code would result in an instance of the OrderMODEL class being retrieved for the user with id request.user .
            #  The order_is_finished attribute is set to False, meaning that this particular instance of the OrderMODEL class has not been finished yet.

        OrderDetails_VAR = OrderDetailsMODEL.objects.all().filter(OrderDetails_order=order_VAR)
        # The iterative loop goes  all products
        for sub in OrderDetails_VAR:
            total_VAR = 0
            # Calculation multiply the price of the product by the quantity
            total_VAR += sub.OrderDetails_price * sub.OrderDetails_quantity
            # Create a new record
            # Put the entered data into the fields
            shipping_adress = CheckoutDetail_MODEL.objects.create(
                address=address, city=city , 
                phone_number=phone_number , 
                state=state, zipcode=zipcode , 
                user=request.user , 
                total_amount=total_VAR , 
                order=order_VAR , 
                payment=payment)
            shipping_adress.save() # Save Data In Table
            #  The code is trying to get the order that is finished.
            #  It does this by getting the OrderMODEL object and then checking if it has an attribute called "is_finished".
            #  If it doesn't have that attribute, then it will set its value to False.
            #  The code would result in an instance of the OrderMODEL class being retrieved for the user with id request.user .
            #  The order_is_finished attribute is set to False, meaning that this particular instance of the OrderMODEL class has not been finished yet.
            order_finished_VAR = OrderMODEL.objects.get(order_user=request.user ,order_is_finished=False)

            order_finished_VAR.order_is_finished = True # user.OrderMODEL Filed Name (order_is_finished) = True

            order_finished_VAR.save() # Save Data in Table
            
            context = {
                    'order_VAR':order_VAR,
                    'OrderDetails_VAR':OrderDetails_VAR,
                    'total_VAR':total_VAR,
                    }
            messages.success(request, "A-Order Is Successfully.")
            return render(request, "checkout/checkout.html", context)
    messages.info(request    , "B")
    return render(request, "checkout/checkout.html")


