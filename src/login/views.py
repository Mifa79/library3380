from itertools import chain
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.models import User, auth
from django.contrib.auth.models import Group
# from .models import Link
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import connection


def myLogin(request):
    with connection.cursor() as cursor:
        if request.method == "POST":

            username = request.POST['username']
            password = request.POST['password']

            # the "aunthenticate" function was written using python and SQL in "authentication.py" in "library3380" folder 
            user = authenticate(request, username=username, password=password)
            # userGroup = user.groups.all()[0]

            if user is not None:
                cursor.execute("SELECT user_type FROM sign_up_user WHERE username= %s", [username])
                user_type = [item[0] for item in cursor.fetchall()]
                print(user_type)

                if(user_type[0] == "1" or user_type[0] == "2"):
                    login(request, user)
                    # print (request.user.is_authenticated)
                    return redirect('/my_login/accountPage')
                else:
                    login(request, user)
                    return redirect('/my_login/employeePage')

            else:
                messages.info(request, 'Invalid Credentials.')
                return redirect('login')

        else:
            return render(request, 'login.html')



@login_required(login_url='/my_login')
def accountPage(request):
    user = request.user
#     globalUrls = Link.objects.filter(links__name='Global')  # returns queryset using foreign key to where group is Global
#     userGroup = user.groups.all()[0]  # object

#     if (userGroup.name != "Global"):
#         userUrls = Link.objects.filter(links__name=userGroup.name)  # queryset
#         links = list(chain(globalUrls, userUrls))  # concat querysets
#         context = {'links': links, 'Role': userGroup.name}
#     else:
#         context = {'links': globalUrls,'Role':userGroup.name}
    context = {'user': user}
    return render(request, 'index.html', context)



@login_required(login_url='/my_login')
def employeePage(request):
    user = request.user
    context = {'user': user}
    return render(request, 'employee_account.html', context)