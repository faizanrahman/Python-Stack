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
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect('/')

    
    var1 = Users.objects.get(email=request.POST['email'])
    if var1.password == request.POST['password']:
        request.session['userid'] = var1.id
        request.session['name'] = var1.first_name
        request.session['loggedin'] = True
        return redirect('/wishes')
    else:
        if 'loggedin' not in request.session:
            request.session['loggedin'] = False
        return redirect('/')
    

def wishes(request):
    if 'loggedin' not in request.session:
        request.session['loggedin'] = False
    if request.session['loggedin'] == True:
        loggeduser = Users.objects.get(id=request.session['userid'])
        userwishes = Wish.objects.filter(uploader=loggeduser)
        context = {
            'userwishes':userwishes,
            'wishes':Wish.objects.all(),
        }
        return render(request, 'loginapp/wishes.html', context)
    else:
        return redirect('/')

#Render New Wish Page
def newWish(request):
    if 'loggedin' not in request.session:
        request.session['loggedin'] = False
    if request.session['loggedin'] == True:
        return render(request, 'loginapp/newwish.html')
#Add a new wish
def addWish(request):
    errors = Wish.objects.wish_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            print(errors)
        
        return redirect('/wishes/new')
    else:
        wish1 = Wish.objects.create(
            item = request.POST['item'],description = request.POST['desc'],uploader = Users.objects.get(id=request.session['userid']))
        request.session['wishid'] = wish1.id
        return redirect('/wishes')

#Edit a wish
def editWish(request, id):
    if 'loggedin' not in request.session:
        request.session['loggedin'] = False
    if request.session['loggedin'] == True:
        wish1 = Wish.objects.get(id=id)
        context = {
            'id':wish1.id,
            'item':wish1.item,
            'description':wish1.description,
        }
        return render(request, 'loginapp/editpage.html', context)
    else:
        return redirect('/')

#Update a Wish
def updateWish(request, id):
    errors = Wish.objects.wish_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request,value)
            print(errors)
        return redirect('/edit/' + str(id))
    else:
        wish1 = Wish.objects.get(id=id)
        wish1.item = request.POST['item']
        wish1.description = request.POST['desc']
        wish1.save()
        return redirect('/wishes')

#Grant a Wish
def granted(request, id):
    #granted_wish = Wish.objects.get(id=id)
    #request.session['granted'] = True
    granted_wish = Wish.objects.get(id=id)
    granted_wish.granted = 1
    granted_wish.save()
    # Wish.objects.all().exclude(id=id)
    # user_wishes = Wish.objects.filter(uploader = request.session['userid'])
    # ungranted_wishes = user_wishes.objects.get(granted=0)
    # print(ungranted_wishes)

    # other_wishes = Wish.objects.all().exclude(granted=0)

    # context = {
    #     'ungranted_wishes':ungranted_wishes,
    #     'other_wishes':other_wishes,
    # }
    return redirect('/wishes')
   
    #     print(request.session['granted'])
    #     # context = {
    #     #     'ungrantedwishes':Wish.objects.all().exclude(granted_wish)
    #     # }
        
    # else:
    #     request.session['granted'] = False
    #     print(request.session['granted'])
    #     return redirect('/wishes')


#Delete a wish
def delete(request, id):
    deleteWish = Wish.objects.get(id=id).delete()
    return redirect('/wishes')




def logout(request):
    request.session['loggedin'] = False
    return redirect('/')