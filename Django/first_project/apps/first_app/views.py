from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    banana = "Hello, I am your first request!"
    return HttpResponse(banana)
