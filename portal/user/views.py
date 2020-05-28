from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import UserRegister,UserLogin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from user.models import UserExt
from django.core.mail import send_mail
from video.forms import VideoForm


def index(request):
    if request.user.is_authenticated:
        user_id = User.objects.get(id=request.user.id)
        user_id = user_id.id
        if UserExt.objects.get(user_id = user_id).activated:
            return render(request,"index.html")
    else:
        return redirect("login")

def upload_video(request):
    if not request.user.is_authenticated:
        messages.warning(request,"To see this video you must login or register firstly!")
        return redirect("login")
    get = UserExt.objects.get(user_id=request.user.id)
    if get.activated == False:
       return redirect("login")
    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Your video is successfuly added!")
        return redirect("home")
    return render(request,"video_upload.html",{"form":form})


def signup(request):
    if request.user.is_authenticated:
        messages.warning(request,"You have already signed up and logged in!")
        return redirect("home")

    form = UserRegister(request.POST or None)
    if form.is_valid():
        username =form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        #confirm = form.cleaned_data['confirm']

        if "fairmont.com" in email:
            newUser = User(username=username,email=email)
            data = User.objects.all()
            for istifadeci in data:
                if email == istifadeci.email:
                    messages.error(request,"This email is already registered!")
                    return redirect("register")
            newUser.set_password(password)
            newUser.save()
            newUser1 = UserExt(user=newUser,activated=False)
            newUser1.save()
            link = "http://localhost:8000/activate/"+str(newUser1.activation_link)
            send_mail("Account Activation","Dear {}, Please use below link to activate your account: {}".format(username,link),"allahverdiulvi@gmail.com",[newUser.email],fail_silently=True)
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Please activate your account!")
            return redirect("login")
        else:
            messages.warning(request,"Unfortunately, This portal allows you to register only with Fairmont.com emails.")
            return redirect("register")
    context = {
        'form':form
    }
    return render(request,'signup.html',context)


def activate_account(request,id):
    UserExt.objects.filter(activation_link=id).update(activated=True)
    messages.success(request,"You account has been activated")
    return redirect("home")

def user_login(request):
    if request.user.is_authenticated:
        messages.warning(request,"You have already logged in!")
        return redirect("home")

    form = UserLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request,username=username,password=password)
        if user is None:
            messages.error(request,"Login or Password is incorrect!")
            return redirect("login")
        login(request,user)
        messages.success(request,"You have successfully logged in!")
        return redirect("/")
    return render(request,"login.html",{"form":form})


def logoff(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You have successfully logged out!")
        return redirect("home")
    else:
        return redirect("")