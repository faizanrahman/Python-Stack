from django.shortcuts import render,redirect, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
   
from apps.loginapp.models import * 

# Create your views here.

def index(request):
    if 'banner' not in request.session:
        request.session['banner'] = 'Please fill the form to register!'
    return render(request,"loginapp/index.html")

def register(request):
    
    errors = Users.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')
    else:
        Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['banner'] = 'Thanks for registering'
            




        return redirect('/')

    









def login(request):
    var1 = Users.objects.get(email=request.POST['email'])
    if var1.password == request.POST['password']:
        request.session['name'] = var1.first_name
        request.session['loggedin'] = True
        return redirect('/success')
    else:
        if 'loggedin' not in request.session:
            request.session['loggedin'] = False
        return redirect('/')
    

def success(request):
    if 'loggedin' not in request.session:
        request.session['loggedin'] = False
    if request.session['loggedin'] == True:
        return render(request, 'loginapp/success.html')
    else:
        return redirect('/')

def logout(request):
    request.session['loggedin'] = False
    return redirect('/')