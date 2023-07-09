from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate 



# Display Login Web Page
# def login_page_DEF(request):
#     return render(request,'login_logout/login.html', {})


def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            remember = request.POST.get('remember_me')
            user = authenticate(username=username, password=password)

            if user is not None:
                if remember is None:
                    request.session.set_expiry(0)  # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.
                    messages.info(request    , "Session Expiry.")
                login(request, user)
                messages.success(request, f'Welcome: ( {username} )')
                return redirect("/")
                # if 'remember_me' not in request.POST:
                #     request.session.set_expiry(0)  # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.
                #     messages.info(request    , "Session Expiry.")
                # login(request, user)
                # messages.success(request, f'Welcome: ( {username} )')
                # return redirect("/")
            else:
                messages.error(request   , "User Name or Password Is Incorrect.") 
                return render(request, "login/login.html")
                # alert = True
                # return render(request, "login/login.html", {"alert":alert})
    return render(request, "login/login.html")
