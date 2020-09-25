from django.shortcuts import render, redirect
from django.http import HttpResponse,request
from.models import client
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def home(request):
    #return HttpResponse("<marquee>hello world</marquee>")
    return render(request,'login.html',{"name":"sdsdsds"})



def signup(request):
    if request.method=="POST":
       
        first_name=request.POST['firstName']
        
        last_name=request.POST['lastName']
        email=request.POST['email']
        x=email.split('@')
        username=x[0]
        password=request.POST['Password']
        gender=request.POST["exampleRadios"]
        dd=request.POST['birthdayDay']
        mm=request.POST['birthdayMonth']
        yy=request.POST['birthdayYear']
        if User.objects.filter(email=email).exists() :
            messages.info(request,'email already exists')
            #return render(request,'signup.html')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'username already exists')
            return render(request,'signup.html')
        else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return render(request,'login.html')
            
        
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print("picked credentials")
       
        user1=auth.authenticate(email=username,password=password)
        user=auth.authenticate(username=username,password=password)
        print(user)
        print("picked auhth")
        if user is not None  :
            print("sucessfully logged in")
            return render(request,'result.html',{'name':username})

        elif user1 is not None:
            print("sucessfully logged in")
            return render(request,'result.html',{'name':username})

        else:
            print('enterd else block')
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
    
    return render(request,'login.html')


