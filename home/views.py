from django.http import response
from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import logout as log_out

# Create your views here.

def home(request):

    return render(request, 'home.html')



def login(request):

    context={
        'form':LoginForm
    }
    return render(request,'login.html', context)



def register(request):

    context={
        'form':RegisterForm
    }
    return render(request,'register.html', context)

# def logout(request):
#     log_out(request)
#     return redirect('/')
