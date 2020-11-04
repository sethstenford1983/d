from django.http import HttpResponse
from app.models import Post
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from  app.models import Client
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
import requests
import json
import random

def login_user(request):
    user = authenticate(
        username = request.POST['username'],
        password = request.POST['password']
    )
    if user is None:
        return render(request,'index.html',{'k':request.user.is_authenticated})
    else:
        login(request, user)
        return HttpResponseRedirect('main_page2')

def index(request):
    return render(request,'index.html',{'k':request.user.is_authenticated, 'title': _('Главная')})

def register(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
    )
    return HttpResponseRedirect('main_page')

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('main_page')
    else:
        return HttpResponseRedirect('main_page')

from django.http import JsonResponse

def ajax_path(request):
    response = {
        'message': request.POST['a'] + 'world'
    }
    return JsonResponse(response)

def index1(request):
    return render(request,'index1.html')

def index2(request):
    return render(request,'index2.html')

def index3(request):
    return render(request, 'index3.html')

#response = requests.get(
    'http://www.nbrb.by/API/ExRates/Currencies'
#)
#data = json.loads(response.text)
#print(data)

from django.utils.translation import ugettext as _
def main(request):
    return render(
        'index.html',
        {'title': _('Главная')}
    )
from django.utils.translation import ugettext as _, activate

def main(request):
    activate('en')
    return render(
        'index.html',
        {'title': _('Главная')}
    )

