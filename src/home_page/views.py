from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

@login_required
def logout(request):
    myLogout(request)
    return redirect('/')
