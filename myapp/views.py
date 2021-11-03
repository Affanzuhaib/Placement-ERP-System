from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method =='POST':
        Username=request.POST['Username']
        pas1=request.POST['pass1']

        user=authenticate(Username=Username,password=pass1)
        if   user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'login.html',{'fname':fname})
        else:
            messages.error(request,"Bad credentails!")
            return redirect(' ')
    return render(request, 'login.html')

def logout(request):
    pass