from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session['unique_id']
    
    if 'redirect' not in request.session: # This is the first time we're coming to the site
        request.session['redirect'] = False
    if request.session['redirect'] == True: # The generate has been pushed and session redirect is true
        if 'counter' in request.session:
            request.session['counter'] += 1
        else:
            request.session['counter'] = 1
        unique_id = get_random_string(length=14)
        request.session['unique_id'] = unique_id # In case it is reloaded we're saving the unique_id as session data to be retrieved at line 22

    else: # If you reload or it's the first time to the site
        if request.session['counter'] == 1:
            unique_id = get_random_string(length=14)
        else:
            unique_id = request.session['unique_id']
    context = {
        "unique_id" : unique_id
    }
    request.session['redirect'] = False
    return render(request,'random_app/index.html', context)

def random(request):
    request.session['redirect'] = True
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    return redirect('/random_word')