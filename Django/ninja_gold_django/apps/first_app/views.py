from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

  # the index function is called when root is visited
def randomNum(start, end):
    num = random.randint(start, end)
    return num

def earn_lose():
    earnOrLose = random.randint(1,2)
    if earnOrLose == 1:
        return True
    else:
        return False




def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'color' not in request.session:
        request.session['color'] = 'green'
    if 'messages' not in request.session:
        request.session['messages'] = []

    return render(request, "first_app/index.html")


def process(request):
    date = datetime.datetime.now()
    if request.POST['building'] == 'farm':
        print('This input is from farm')
        randomNumFarm = randomNum(10,20)
        request.session['total']+=randomNumFarm
        activity = "Earned " + str(randomNumFarm) + " golds" + " from the farm" "                                                                                                          " + str(date)
        activity_list = request.session['messages']
        activity_list.append({"activity":activity, 'color':'green'})
        request.session['messages'] = activity_list
        print(randomNumFarm)
    elif request.POST['building'] == 'cave':
        print('This input is from cave')
        randomNumCave = randomNum(5,10)
        request.session['total']+=randomNumCave
        activity = "Earned " + str(randomNumCave) + " golds" + " from the cave" "                                                                                                          " + str(date)
        activity_list = request.session['messages']
        activity_list.append({"activity":activity, 'color':'green'})
        request.session['messages'] = activity_list
        print(randomNumCave)
    elif request.POST['building'] == 'house':
        print('This input is from house')
        randomNumHouse = randomNum(2,5)
        request.session['total']+=randomNumHouse
        activity = "Earned " + str(randomNumHouse) + " golds" + " from the house" "                                                                                                          " + str(date)
        activity_list = request.session['messages']
        activity_list.append({"activity":activity, 'color':'green'})
        request.session['messages'] = activity_list
        print(randomNumHouse)
    elif request.POST['building'] == 'casino':
        print('This input is from casino')
        randomNumCasino = randomNum(0,50)
        if earn_lose() == True:
            request.session['total']+=randomNumCasino
            activity = "Earned " + str(randomNumCasino) + " golds" + " from the casino" "                                                                                                          " + str(date)
            activity_list = request.session['messages']
            activity_list.append({"activity":activity, 'color':'green'})
            request.session['messages'] = activity_list        
        elif earn_lose() == False:
            request.session['total']-=randomNumCasino
            #request.session['color'] = 'red'
            activity = "Lost " + str(randomNumCasino) + " golds" + " from the casino" "                                                                                                          " + str(date)
            activity_list = request.session['messages']
            activity_list.append({"activity":activity, 'color':'red'})
            request.session['messages'] = activity_list
        print(randomNumCasino)
    print(request.session['total'])
    request.session['messages'] = request.session['messages'][::-1]


    if request.POST['building'] == 'reset':
        request.session.clear()

    return redirect('/') 
