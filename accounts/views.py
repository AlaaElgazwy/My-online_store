from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
# Create your views here.

def register_view(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        

        user=User.objects.create_user(username=username,password=password)
        user.save()
        messages.success(request,'register is success')
        return redirect('login')

    return render (request,'register.html') 

def login_view(request):

    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password) 
        if user is not None:
            login(request,user)
        return redirect('profile')
    else:
        messages.error(request,'data of login not true')
    
    return render(request,'login.html')

def logout_view(request):

    logout(request)
    return redirect('login') 