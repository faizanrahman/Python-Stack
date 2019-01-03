from django.shortcuts import render,HttpResponse, redirect
from time import strftime, localtime

# Create your views here.
def index(request):
    return render(request,'first_app/index.html')

def add_word(request):
    timenow = strftime('%#H:%M:%S%p, %B %#d %Y', localtime())
    #print(request.POST)
    # if 'word' not in request.session:
    #request.session['word'] = request.POST['word']
    #     request.session['word'] = [{"word": "request.POST['word']", "color":"request.POST['color]", "font": "request.session['font']"}]
    # temp_list = request.session['word']
    # temp_list.append({"word": request.POST['word'], "color":request.POST['color'], "font": request.session['font']})
    # request.session['word'] = temp_list
    if 'words' not in request.session:
        request.session['words'] = []

    # if 'big_font' in request.POST:
    temp_list = request.session['words']
    if request.POST['font'] == '1':
        data = {'word': request.POST['word'],'color': request.POST['color'],'font': '24px','time': timenow}
    else:
        data = {'word': request.POST['word'],'color': request.POST['color'],'font': '12px','time': timenow}
    
    temp_list.append(data)
    reversed = temp_list[::-1]
    request.session['words'] = reversed
    # request.session['words'][::-1]

    # request.session['words'].append(data)
    print(request.session['words'])
    # if 'color' not in request.session:
    #     request.session['color'] = request.POST['color']
    # if 'font' not in request.session:
    #     request.session['font'] = request.POST['font']
    # if request.session['font'] == 1:
    #     request.session['font'] = '32px'

    
    
    return redirect('/')

def clear(request):
    del request.session['words']
    return redirect('/')
