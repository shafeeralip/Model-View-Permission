from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate
from django.contrib.auth import  login as auth_login
from django.contrib.auth import  logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Primeuser
from django.contrib.auth.models import Group
from .decorators import uauthenticateduser,alloweduser

# Create your views here.

@uauthenticateduser
def login(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        if user:
            auth_login(request, user)

            if user.has_perm('app.view_primeuser'):
                print("working")
            else:
                print("not working")
        
    
            return redirect(home)
        else:
            messages.info(request,'invalid credention')

    
    return render(request,'login.html')

@uauthenticateduser
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
def home(request):
    print(request.user)
    if request.user.has_perm('app.view_primeuser'):
        print("working ")
    else:
        print("not working")
    return render(request,'home.html')


@login_required(login_url='/')
@alloweduser(allowed_roles=['primeuser'])
def profile(request):
    return render(request,'profile.html')


@login_required(login_url='/')
@alloweduser(allowed_roles=['primeuser'])
def history(request):
    return render(request,'history.html')
    
@login_required(login_url='/')
def logout(request):
    auth_logout(request)
    return redirect(login)

@login_required(login_url='/')
@alloweduser(allowed_roles=['Staff','admin'])
def users(request):

    us=User.objects.filter(is_staff=False)
    users=[]
    for user in us:
        if Primeuser.objects.filter(User=user).exists():
            pass
        else:
            users.append(user)
    return render(request,'user.html',{'users':users})

@login_required(login_url='/')
@alloweduser(allowed_roles=['admin'])
def staff(request):
    staffs=User.objects.filter(is_staff=True,is_superuser=False)
    
    return render(request,'staff.html',{'staffs':staffs})

@login_required(login_url='/')
@alloweduser(allowed_roles=['Staff','admin'])
def prime(request):
    primeusers=Primeuser.objects.all()


    return render(request,'primeuser.html',{'primeusers':primeusers})

@login_required(login_url='/')
@alloweduser(allowed_roles=['Staff','admin'])
def addstaff(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=name,email=email,password=password,is_staff=True)
        user.save()
        my_group = Group.objects.get(name='Staff')
        my_group.user_set.add(user)
        return redirect(staff)
    return render(request,'addstaff.html')

@login_required(login_url='/')
@alloweduser(allowed_roles=['Staff','admin'])
def adduser(request):
    if request.method=='POST':
        name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create_user(username=name,email=email,password=password)
        user.save()
        return redirect(users)
    return render(request,'adduser.html')

@login_required(login_url='/')
@alloweduser(allowed_roles=['Staff','admin'])
def edituser(request,id):
    user=User.objects.get(id=id)
    if request.method=='POST':
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.save()
        return redirect(users)

    

    return render(request,'edituser.html',{'user':user})

@login_required(login_url='/')
@alloweduser(allowed_roles=['Staff','admin'])
def addprimeuser(request,id):
    user=User.objects.get(id=id)
    primeuser=Primeuser.objects.create(User=user)
    my_group = Group.objects.get(name='primeuser')
    my_group.user_set.add(user)
    return redirect(prime)

@login_required(login_url='/')
@alloweduser(allowed_roles=['Staff','admin'])
def editprimeuser(request,id):
    primeuser=Primeuser.objects.get(id=id)
    user=User.objects.get(username=primeuser.User.username)

    if request.method=='POST':
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.save()
        return redirect(prime)



    return render(request,'editprime.html',{'primeuser':primeuser})

@login_required(login_url='/')
@alloweduser(allowed_roles=['admin'])
def delete(request,id,value):
    
   
    if value=='staff':
        User.objects.filter(id=id).delete()
        return redirect(staff)
    elif value=='prime':
        Primeuser.objects.filter(id=id).delete()
        return redirect(prime)
    else:
        User.objects.filter(id=id).delete()
        return redirect(users)

