from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
  # the index function is called when root is visited
def index(request):
    context = {
        "time1": strftime("%a, %d %b %Y", gmtime()),
        "time2": strftime("%I:%M %p", gmtime())
    }
    return render(request,'timedisplay/index.html', context)