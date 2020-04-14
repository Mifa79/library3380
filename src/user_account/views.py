from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required
from django.db import connection
from datetime import date
from datetime import datetime, timedelta
from django.contrib import messages

# Create your views here.
@login_required(login_url='/my_login')
def userAccount(request):
    with connection.cursor() as cursor:
        user = request.user
        print("user is: ", user)

        # get user info from the database
        cursor.execute("SELECT id, user_type FROM sign_up_user WHERE username= %s", [user])
        user_info = dictfetchall(cursor)
        user_info = user_info[0]
        print ("user info is: ", user_info)
        print("user_ID is: ", user_info['id'])
        user_ID = user_info['id']
        print("user type is: ", user_info['user_type'])
        user_type = user_info['user_type']

        context = {'user': user}
        return render(request, 'user_account.html', context)

@login_required
def logout(request):
    myLogout(request)
    return redirect('/')



def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]