from django.shortcuts import render

# Create your views here.


def signup(request):
    return render(request, 'account/signup.html')


def login(request):
    return render(request, 'account/login.html')


def signout(request):
    # TODO need to route to homepage
    return render(request, 'account/signup.html')
