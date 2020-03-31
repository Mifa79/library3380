from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

def sign_up(request):
    if request.method == 'POST':
        print("yeah")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        

        if first_name == '':
            messages.info(request, '**ERROR: First Name is required')
        if last_name == '':
            messages.info(request, '**ERROR: Last Name is required')
        if User.objects.filter(username=username).exists():
            messages.info(request, '**ERROR: Username already exists')
        if username == '':
            messages.info(request, '**ERROR: Username is required')
        if User.objects.filter(email=email).exists():
            messages.info(request, '**ERROR: Email already taken')
        if email == '':
            messages.info(request, '**ERROR: Email address is required')
        if password1 != password2:
            messages.info(request, '**ERROR: Password not matching')
        if password1 == '':
            messages.info(request, '**ERROR: Password is required')
        if password1 == password2 and (not User.objects.filter(username=username).exists()) \
                and (not User.objects.filter(email=email).exists()) and (password1 != '') and (first_name != '')\
                and (last_name != '') and (username != '') and (email != ''):
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                                last_name=last_name)
            user.save()
            return render(request, 'sign_up_success.html')

        return redirect('sign_up')

    else:
        return render(request, 'sign_up.html')
