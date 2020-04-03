from itertools import chain
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group, Permission
# from .models import Link
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        # the "aunthenticate" function was written using python and SQL in "authentication.py" in "library3380" folder 
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            
            return redirect('sign_up_success.html')
        else:
            messages.info(request, 'Invalid Credentials.')
            return redirect('/')

    else:
        return render(request, 'login.html')


# @login_required(login_url='/')
# def accountPage(request):
#     user=request.user
#     globalUrls = Link.objects.filter(links__name='Global')  # returns queryset using foreign key to where group is Global
#     userGroup = user.groups.all()[0]  # object

#     if (userGroup.name != "Global"):
#         userUrls = Link.objects.filter(links__name=userGroup.name)  # queryset
#         links = list(chain(globalUrls, userUrls))  # concat querysets
#         context = {'links': links, 'Role': userGroup.name}
#     else:
#         context = {'links': globalUrls,'Role':userGroup.name}
#     return render(request, 'account.html', context)
