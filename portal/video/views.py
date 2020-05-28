from django.shortcuts import render,redirect
from .models import Video
from user.models import UserExt
from django.contrib import messages

def videos(request):
    if not request.user.is_authenticated:
        messages.warning(request,"To see this video you must login or register firstly!")
        return redirect("login")
    get = UserExt.objects.get(user_id=request.user.id)
    if get.activated == False:
       return redirect("login")
    data = Video.objects.all()
    return render(request,"media.html",{"data":data})


def video_detail(request,id):
    if not request.user.is_authenticated:
        messages.warning(request,"To see this video you must login or register firstly!")
        return redirect("login")
    get = UserExt.objects.get(user_id=request.user.id)
    if get.activated == False:
       return redirect("login")
    data = Video.objects.get(id=id)
    return render(request,"detail.html",{"data":data})
