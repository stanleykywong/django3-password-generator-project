from django.shortcuts import render

# 1) added by  ourselves
from django.http import HttpResponse

import random

# Create your views here.

# 2) make views.home
def home(request):
    # return HttpResponse("Hello there friend!")

    # step 1
    # return render(request, 'generator/home.html', {'password':'qwert'})
    return render(request, 'generator/home.html')

# 2) make views.eggs
# def eggs(request):
#     return HttpResponse("<h1>Eggs are so tasty</h1>")

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    # thepassword = 'testing'

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # length = 10
    # *** in the URL, there's a 'length' we can grab; 12 is our default value
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)    # random.choice

    return render(request, 'generator/password.html', {'password':thepassword})
