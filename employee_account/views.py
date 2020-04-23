from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/my_login')
def employeePage(request):
    user = request.user
    context = {'user': user}
    return render(request, 'employee_account.html', context)

@login_required
def logout(request):
    myLogout(request)
    return redirect('/')