from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout 



# Display Login Web Page
def login_page_DEF(request):
    return render(request,'login_logout/login.html', {})


def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                alert = True
                return render(request, "login/login.html", {"alert":alert})
    return render(request, "login/login.html")
