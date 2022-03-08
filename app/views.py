from django.shortcuts import render, redirect
from .models import UserReg
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.method=='POST':
        u_name= request.POST['username']
        u_email= request.POST['useremail']
        u_pwd= request.POST['userpass']
        if u_name and u_pwd and u_email !='':
            if len(u_pwd)>3:
                set_query= UserReg (name=u_name, email=u_email, password=u_pwd)
                set_query.save()
                messages.info(request, 'saved')
                return redirect('login')
            else:
                messages.info(request,"password should be 8 characters")
                return render(request, 'index.html')
        else:
            messages.info(request, 'All fields are required')
            return render(request, 'index.html')
    return render(request, 'index.html')

def login(request):
    if request.method== 'POST':
        username = request.POST['input_email']
        password = request.POST['input_pwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("login")
        else:
            return HttpResponse("Invalid")

    return render(request, 'login.html')