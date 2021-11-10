from django.http.request import HttpHeaders
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(username,fname,lname)

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_superuser = False
        myuser.is_staff = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
    return render(request,'signup.html')
    #return HttpResponse('This is signup page')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request,"signup.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')
    
    return render(request, "signin.html")
  #return render(request,'signin.html')
