from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth.models import Group


def  unauthenticated_user(view_fuc):
    def wrapper_fuc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("live")
        else:
            return HttpResponse("sample")
    return wrapper_fuc


def allowed_users(allowed_roles=[]):
    def  decorator(view_fuc):
        def wrapper_fuc(request, *args, **kwargs):
            group = None
            abc = Group.objects.filter(name = allowed_roles[0])
            print(abc)
            if Group.objects.filter(name = allowed_roles[0]):
                print("valid user")
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            return HttpResponse("You are valid")
            # if group in allowed_roles:
            #     return view_fuc(request, *args, **kwargs)
            # else:
            #     return HttpResponse("You are not authorized")
        return wrapper_fuc
    return decorator