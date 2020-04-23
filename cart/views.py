from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required


def cart(request):
    return render(request, 'cart.html')


@login_required
def logout(request):
    myLogout(request)
    return redirect('/')