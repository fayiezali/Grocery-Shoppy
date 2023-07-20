from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
import re
#
# validation formula
EMAIL_REGEX        = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
USERNAME_REGEX     = re.compile("[a-z0-9_]{3,15}")
FIRSTNAME_REGEX    = re.compile("[a-zA-Z]{2,20}")
LASTNAME_REGEX     = re.compile("[a-zA-Z]{2,20}")
PASSWARD_Criterian = {
                    "length_criteria":".{8,}",
                    "lowercase_criteria":"[a-z]+",
                    "uppercase_criteria":"[A-Z]+",
                    "number_criteria":"[0-9]+",
                    "symbol_criteria":"[^A-Za-z0-9]+",
                    }
#
#
# VER:Variables        
def Signup_DEF(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        # Verify the validity of the entered data
        # if request.method == "POST":
        if request.method == "POST" and  'button_signup' in request.POST:
            # USER Model Fields:--------------------------------------------
            user_name_VAR             = request.POST['user_name']
            user_password_VAR         = request.POST['user_password']
            user_confirm_password_VAR = request.POST['user_confirm_password']
            email_VAR                 = request.POST['email']
            first_name_VAR            = request.POST['first_name']
            last_name_VAR             = request.POST['last_name']
            # PROFILE Model Fields:-------------------------------------------
            father_name_VAR           = request.POST['father_name']
            grand_father_name_VAR     = request.POST['grand_father_name']
            mobile_number_VAR         = request.POST['mobile_number']
            # ---------------------------------------------------------------
            # defining some parameter for user to follow while making account
            # Verify the validity of the inputs - UserName
            if not USERNAME_REGEX.match(user_name_VAR):
                # Display a message to the user
                messages.error(request, "User Name - The Entered Data Is incorrect") 
                return redirect('signup-URL')

            # Verify that the name is not used by another user
            if User.objects.filter(username=user_name_VAR):
                # Display a message to the user
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('signup-URL')

            # Verify the number of input letters
            if len(user_name_VAR)>20:
                # Display a message to the user
                messages.error(request, "Username must be under 20 charcters!!")
                return redirect('signup-URL')

            # Verify the validity of the inputs - Email
            if not EMAIL_REGEX.match(email_VAR):
                # Display a message to the user
                messages.error(request, "EMAIL - The Entered Data Is incorrect")
                return redirect('signup-URL')

            # Verify that the Email is not used by another user
            if User.objects.filter(email=email_VAR).exists():
                # Display a message to the user
                messages.error(request, "Email Already Registered!!")
                return redirect('signup-URL')

            # Check the passwords match
            if user_password_VAR != user_confirm_password_VAR:
                # Display a message to the user
                messages.error(request, "Passwords didn't Matched!!")
                # Return Redirect To This Page
                return redirect('signup-URL')
            # ---------------------------------------------------------------
            user_VAR = User.objects.create_user(username=user_name_VAR , 
                                            password=user_password_VAR , 
                                            email=email_VAR ,
                                            first_name=first_name_VAR ,
                                            last_name=last_name_VAR
                                            )
            profile_VAR = UserProfile_MODEL.objects.create(pro_User=user_VAR ,
                                                    Pro_FatherName=father_name_VAR ,
                                                    Pro_GrandFatherName=grand_father_name_VAR ,
                                                    Pro_MobileNnumber=mobile_number_VAR
                                                    )
            user_VAR.save() # save Data In Table 01
            profile_VAR.save() # save Data In Table 02
            # Display a message to the user
            messages.success(request, f'Welcome: ( {user_name_VAR} ) - Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.')
            # Return Redirect To This Page
            return render(request, "login/login.html")
    # If the current condition is met: (request.method == "POST" and  'button_signup' in request.POST:)Return Redirect To This Page
    return render(request, "signup/signup.html")
