from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate
from django.contrib.auth import  login as auth_login
from django.contrib.auth import  logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        if user:
            auth_login(request, user)
            if user.has_perm('app.prime user_primeuser'):
                prin
            if user.is_staff:
                pass
            else:
                return redirect(userhome)
        else:
            messages.info(request,'invalid credention')

    
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=name,email=email,password=password)
        user.save()
        return redirect(login)

    return render(request,'register.html')
@login_required(login_url='/')
def userhome(request):
    print(request.user)
    if request.user.has_perm('app.view_Primeuser'):
        print("working ")
    else:
        print("not working")
    return render(request,'home.html')

@login_required(login_url='/')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='/')
def history(request):
    return render(request,'history.html')
    
@login_required(login_url='/')
def logout(request):
    auth_logout(request)
    return redirect(login)