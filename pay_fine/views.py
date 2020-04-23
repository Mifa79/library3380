from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime, timedelta
from django.contrib import messages

def pay_fine(request):
      with connection.cursor() as cursor:
        if request.method == "POST":
            fine_ID = request.POST['fine_ID']
            loan_ID = request.POST['loan_ID']
            amount_due = request.POST['amount_due']

            # update "paid" to 1 in fine table 
            cursor.execute("UPDATE fine SET paid=1 WHERE fine_ID = %s", [fine_ID])
            row = cursor.fetchall()

            messages.info(request, "You have successfully paid fine " + fine_ID)


            return redirect("userAccount")
        else:
            return redirect("userAccount")