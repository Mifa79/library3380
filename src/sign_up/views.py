from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.db import connection

def sign_up(request):
    with connection.cursor() as cursor:

        if request.method == 'POST':
            print("yeah")
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            user_type = request.POST['user_type']       

            if first_name == '':
                messages.info(request, '**ERROR: First Name is required')

            if last_name == '':
                messages.info(request, '**ERROR: Last Name is required')

            cursor.execute("SELECT COUNT(user_name) FROM user WHERE user_name = %s", [username])
            user_name_num = [item[0] for item in cursor.fetchall()]
            if user_name_num[0] > 0:
                messages.info(request, '**ERROR: Username already exists')

            if username == '':
                messages.info(request, '**ERROR: Username is required')

            cursor.execute("SELECT COUNT(user_email) FROM user WHERE user_email = %s", [email])
            user_email_num = [item[0] for item in cursor.fetchall()]
            if user_email_num[0] > 0:
                messages.info(request, '**ERROR: Email already taken')

            if email == '':
                messages.info(request, '**ERROR: Email address is required')

            if password1 != password2:
                messages.info(request, '**ERROR: Password not matching')

            if password1 == '':
                messages.info(request, '**ERROR: Password is required')

            if password1 == password2 and (user_name_num[0] == 0) and (user_email_num[0] == 0) and (password1 != '') and (first_name != '')\
                    and (last_name != '') and (username != '') and (email != ''):


                cursor.execute("INSERT INTO user (fname, lname, user_name, user_email, user_password, user_type_ID)\
                                VALUE (%s, %s, %s, %s, %s, %s)", [first_name, last_name, username, email, password1, user_type])
                row = cursor.fetchall()
                # return row



                # user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                #                                     last_name=last_name)
                # user.save()
                return render(request, 'sign_up_success.html')

            return redirect('sign_up')

        else:
            return render(request, 'sign_up.html')
