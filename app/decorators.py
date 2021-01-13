from django.shortcuts import redirect
from django.http import  HttpResponse

def uauthenticateduser(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    
    return wrapper_func



def alloweduser(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            groups=None
            flag=True

            if request.user.groups.exists():
                groups=request.user.groups.values_list('name',flat=True)
                print(groups)
                for group in groups:
                    print(group)
                    if group in allowed_roles:
                        flag=False
                        return view_func(request,*args,**kwargs)
                if flag:
                    return HttpResponse("you are not autherized to acess this page")
            else:
                return HttpResponse("you are not autherized to acess this page")

        return wrapper_func
    return decorator
