from django.shortcuts import render,redirect, HttpResponse
from apps.first_app.models import *

# Create your views here.
def index(request):
    context =  {
        'users' : Users.objects.all()
    }
    return render(request,"first_app/index.html", context)

def new(request):
    return render(request, "first_app/newuser.html")

def update(request, id):
    context = {
        'id' : id,
        'users' : Users.objects.get(id=str(id))
    }
    return render(request,"first_app/edituser.html", context)

def show(request, id):
    context = {
        'id' : id,
        'users' : Users.objects.get(id=str(id))
    }
    return render(request,"first_app/showuser.html", context)
# Method that will actually create the new user.
def create(request):
    
    Users.objects.create(first_name= request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    
    return redirect('/users')

def updated(request):
    editID = request.POST['hiddenid']
    editUser = Users.objects.get(id=editID)
    print(editUser)
    editUser.first_name = request.POST['first_name']
    editUser.last_name = request.POST['last_name']
    editUser.email = request.POST['email']
    editUser.save()
    print(editUser)
    # context = {
    #     'id':editID,
    #     #'users':Users.objects.get(id=str(id))
    #     'users': editUser
    # }
    return redirect('/users/' + request.POST['hiddenid'])


def delete(request, id):

    deleteUser = Users.objects.get(id=id).delete()
    return redirect('/users')
    
