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

        # get all the active loans of the user
        cursor.execute("SELECT loan_ID, item_ID, item_copy_ID, borrow_date, return_due_date FROM loan WHERE user_ID = %s", [user_ID])
        all_active_loans = dictfetchall(cursor)
        print("all_active_loan is: ", all_active_loans)

        # get all the past loans of the user
        cursor.execute("SELECT loan_ID, item_ID, item_copy_ID, borrow_date, return_due_date, overdue_date_num, damaged, lost FROM loan WHERE user_ID = %s", [user_ID])
        all_past_loans = dictfetchall(cursor)
        print("all_past_loans is: ", all_past_loans)

        # get all the active fines of the user
        cursor.execute("SELECT fine_ID, loan_ID, amount_due FROM fine WHERE user_ID = %s and paid=0", [user_ID])
        all_unpaid_fines = dictfetchall(cursor)
        print("all_unpaid_fines are: ", all_unpaid_fines)


        # get all the complete fines of the user
        cursor.execute("SELECT fine_ID, loan_ID, amount_due FROM fine WHERE user_ID = %s and paid=1", [user_ID])
        all_paid_fines = dictfetchall(cursor)
        print("all_paid_fines are: ", all_paid_fines)

        context = {'user': user, 'all_active_loans': all_active_loans, 'all_unpaid_fines': all_unpaid_fines, 'all_past_loans': all_past_loans, 'all_paid_fines': all_paid_fines}
        return render(request, 'user_account.html', context)


# @login_required(login_url='/my_login')
# def return_item(request):
#     with connection.cursor() as cursor:
#         if request.method == "POST":


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