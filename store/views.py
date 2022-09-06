from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import * 
from store.forms import *



# Create your views here.

def login(request):
    return render(request,'login.html')

def success(request):
    email=request.POST.get('email')
    pwd=request.POST.get('pwd')
    try:
        if user.objects.filter(email=email,pwd=pwd).exists():
            return render(request,'welcome.html')
        else:
            return render(request,'login.html')
    except:
        return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')

def db_update(request):
    u=user()
    try:
        u.name=request.POST.get('name')
        u.email=request.POST.get('email')
        u.pincode=request.POST.get('pincode')
        u.phno=request.POST.get('phno')
        u.pwd=request.POST.get('pwd')
        u.save()
        return render(request,'login.html')
    except Exception as e:
        return HttpResponse(e)


