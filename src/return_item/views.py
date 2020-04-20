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

            if 'damaged' not in request.POST:
                damaged = 0
            else:
                damaged = 1

            if 'lost' not in request.POST:
                lost = 0
            else:
                lost = 1

            print("damaged is", damaged)
            print("lost is", lost)

            today = date.today()
            print(today)

            # return_due_date = datetime.strptime(return_due_date, '%B %d %Y')
            # print(return_due_date)

            # if today > return_due_date:
            #     overdue_date_num = today - return_due_date
            #     print(overdue_date_num)
            # else:
            #     overdue_date_num = 0

            overdue_date_num = 0

            # update "loan" table if no damage and no lost
            if (damaged==0 and lost==0):
                cursor.execute("UPDATE loan SET active=0, damaged=0, lost=0, overdue_date_num = %s WHERE loan_ID = %s", [overdue_date_num, loan_ID])
                row = cursor.fetchall()

            # update "loan" table if item is lost (no late or damaged fine applied)
            if lost==1:
                cursor.execute("UPDATE loan SET active=0, damaged=0, lost=1, overdue_date_num=0 WHERE loan_ID = %s", [loan_ID])
                row = cursor.fetchall()

            if (damaged==1 and lost==0):
                cursor.execute("UPDATE loan SET active=0, damaged=1, lost=0, overdue_date_num=0 WHERE loan_ID = %s", [loan_ID])
                row = cursor.fetchall()

            # update damaged, lost, and "loaned" to 0 in "copy" table
            cursor.execute("UPDATE copy SET loaned=0, damaged = %s, lost = %s WHERE item_ID = %s and copy_ID = %s", [damaged, lost, item_ID, copy_ID])
            row = cursor.fetchall()

            if (damaged==0 and lost==0 and overdue_date_num==0):
                messages.info(request, "You have successfully returned the item. Loan " + loan_ID + " is now complete.")
            if (damaged==0 and lost==0 and overdue_date_num>0):
                messages.info(request, "You have successfully returned the item. Loan " + loan_ID + " is now complete. However, since you returned the item late, fine will be applied. Please check out My Account page for details.")
            if lost==1:
                messages.info(request, "Loan " + loan_ID + " is now complete. However, since you lost the item, fine will be applied according to the market price of the item. Please check out My Account page for details.")
            if (damaged==1 and lost==0):
                messages.info(request, "You have successfully returned the item. Loan " + loan_ID + " is now complete. However, since you damaged the item, fine will be applied. Please check out My Account page for details.")

            return redirect("userAccount")
        else:
            return redirect("userAccount")