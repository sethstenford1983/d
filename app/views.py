from django.http import HttpResponse
from app.models import Post
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from  app.models import Client
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect

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
    return render(request,'index.html',{'k':request.user.is_authenticated})

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




