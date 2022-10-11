from django.shortcuts import render , HttpResponse, redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.views.decorators.http import require_http_methods


# Create your views here.
def user_login(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')




@require_http_methods(['POST'])
def user_auth(request):
    uname = request.POST.get('username')
    pwd = request.POST.get('password')

    user = authenticate(username = uname , password = pwd)

    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        return HttpResponse('Username/password incorrect')



def user_registration(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            email = form.cleaned_data['email']
            psw = form.cleaned_data['password']

            User.objects.create_user(username=un , email= email , password= psw)

            return redirect('login')


    else:
        form = registrationform()
    return render(request , 'register.html')

def index_page(request):
    return render(request , 'index.html')