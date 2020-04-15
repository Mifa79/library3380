from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime, timedelta
from django.contrib import messages

def return_item(request):
      with connection.cursor() as cursor:
        if request.method == "POST":
            loan_ID = request.POST['loan_ID']
            item_ID = request.POST['item_ID']
            copy_ID = request.POST['copy_ID']
            return_due_date = request.POST['return_due_date']

            # today = date.today()
            # print(today)
            # overdue_date_num = today - return_due_date
            # print(overdue_date_num)

            overdue_date_num = 10

            # update loan" table
            cursor.execute("UPDATE loan SET active=0, overdue_date_num = %s WHERE loan_ID = %s", [overdue_date_num, loan_ID])
            row = cursor.fetchall()

            # update "loaned" to 0 in "copy" table
            cursor.execute("UPDATE copy SET loaned=0 WHERE item_ID = %s and copy_ID = %s", [item_ID, copy_ID])
            row = cursor.fetchall()



            

            messages.info(request, "You have successfully returned the book. Loan " + loan_ID + " is now complete.")
            return redirect("userAccount")
        else:
            return redirect("userAccount")