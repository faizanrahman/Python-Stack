from django.shortcuts import render,redirect, HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db import models
   
from .models import *

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
        request.session['userid'] = var1.id
        request.session['name'] = var1.first_name
        request.session['loggedin'] = True
        return redirect('/quotes')
    else:
        if 'loggedin' not in request.session:
            request.session['loggedin'] = False
        return redirect('/')
    

def quotes(request):
    if 'loggedin' not in request.session:
        request.session['loggedin'] = False
    if request.session['loggedin'] == True:
        context = {
            'quotes': Quotes.objects.all(),
            'users' : Users.objects.all(),
        }
        # print(Quotes.objects.all().values())
        return render(request, 'loginapp/quotes.html', context)
    else:
        return redirect('/')

def logout(request):
    request.session['loggedin'] = False
    return redirect('/')


#Add Quote
def add_quote(request):
    errors = Quotes.objects.quote_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            print(errors)
        
        return redirect('/quotes')
    else:
        quote1 = Quotes.objects.create(author=request.POST['author'], quote_text=request.POST['user_quote'], uploader=Users.objects.get(id=request.session['userid']))
        request.session['quoteid'] = quote1.id
        print(request.session['quoteid'])     
        # print(request.POST['author'])
        # print(request.POST['user_quote'])
        return redirect('/quotes')

#Show User Quotes
def showuser(request, id):
    if 'loggedin' not in request.session:
        request.session['loggedin'] = False
    if request.session['loggedin'] == True:
    # context = {
    #     'id' : id,
    #     'users' : Users.objects.get(id=id))
    # }
        user2 = Users.objects.get(id=id)
        userQuote = Quotes.objects.filter(uploader=user2)
        context = {
            'userQuote':userQuote,
        }
        return render(request, 'loginapp/showuser.html', context)
    else:
        return redirect('/')

#Edit Page
def edituser(request, id):
    
    if 'loggedin' not in request.session:
        request.session['loggedin'] = False
    if request.session['loggedin'] == True:
        user1 = Users.objects.get(id=id)
        context = {
            "id": user1.id,
            "first_name": user1.first_name,
            "last_name": user1.last_name,
            "email": user1.email,
        }

        return render(request, "loginapp/edituser.html", context)
    else:
        return redirect('/')


#Update Page
def updateuser(request, id):
    user1 = Users.objects.get(id=id)
    user1.first_name = request.POST['first_name']
    user1.last_name = request.POST['last_name']
    user1.email = request.POST['email']
    user1.save()
    request.session['name'] = user1.first_name
    return redirect('/quotes')
#Delete Page 
def delete(request, id):
    deleteQuote = Quotes.objects.get(id=id).delete()
    return redirect('/quotes')


#Add Likes

def likes(request, id):
    quote = Quotes.objects.get(id=request.session['quoteid'])
    count = quote.likes.count()
    counter = count + 1
    context = {
        "counter": counter
    }
    userLiking = request.session['userid']
    quote = Quotes.objects.get(id=id)
    user1 = Users.objects.get(id= userLiking)
    quote.likes.add(user1)
    quote.save()
    #print (quote.likes.all().values())
    return redirect("/quotes")