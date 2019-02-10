from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                # user (can i delete this variable?)
                User.objects.get(username=request.POST['username'])
                return render(request, 'account/signup.html', {'error': 'username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'account/signup.html', {'error': 'password must match'})

    else:
        return render(request, 'account/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'account/login.html', {'error': 'username or password is incorret'})
    else:
        return render(request, 'account/login.html')


def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
