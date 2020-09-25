from django.shortcuts import render
from .models import doctors
import os
# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    print(os.getcwd())
    doc=doctors.objects.all()
    return render(request,'home.html',{"doc":doc})
    print(os.getcwd())


def profile(request):
    return render(request,'profile.html' )

def replies(request):
    return render(request,'replies.html')

def login(request):
    return render(request,'login.html')