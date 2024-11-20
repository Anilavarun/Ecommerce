from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        username=request.POST['username']
        password=request.POST['password']
        repsw=request.POST['repassword']
        if password==repsw:
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username Taken')
               return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,username=username,password=password)
                user.save();
                return redirect('login')
        else:
           messages.info(request,'Passwords do not match')
           return redirect('register')
    else:

        return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
           auth.login(request,user)
           return redirect('home')
        else:
            message.info(request,'Invalid username or password')
            return redirect('login')
    else:
        return render(request,"log.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


