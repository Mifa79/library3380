from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime, timedelta
from django.contrib import messages

def book_borrow(request):
    with connection.cursor() as cursor:
        if request.method == "POST":
            ISBN = request.POST['ISBN']
             # get all the details of the book
            cursor.execute("SELECT ISBN, book_title, book_author, book_subject, book_publisher, date_of_publication, MSRP FROM book WHERE ISBN= %s", [ISBN])
            book_details = dictfetchall(cursor)
            book_detail = book_details[0]
            print("Book Details is: ", book_detail)

            # check number of available copies:
            cursor.execute("SELECT COUNT(copy_ID) FROM copy where item_ID= %s and loaned=0 and damaged=0 and lost=0", [ISBN])
            num_of_copies_available = cursor.fetchone()
            num_of_copies_available = num_of_copies_available[0]
            print("num_of_copies_available is: ", num_of_copies_available)
            
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

            # get user type info from the database
            cursor.execute("SELECT borrow_time_limit, borrow_amount_limit, reservation_amount_limit FROM user_type_info WHERE user_type_ID= %s", [user_type])
            user_type_info = dictfetchall(cursor)
            user_type_info = user_type_info[0]
            print("user_type_info is: ", user_type_info)
            borrow_time_limit = user_type_info['borrow_time_limit']
            print("borrow_time_limit is: ", borrow_time_limit)
            borrow_amount_limit = user_type_info['borrow_amount_limit']
            reservation_amount_limit = user_type_info['reservation_amount_limit']

            # count the number of active loan of the user
            cursor.execute("SELECT COUNT(loan_ID) FROM loan where user_ID = %s and active=0", [user_ID])
            num_of_active_loan = cursor.fetchone()
            num_of_active_loan = num_of_active_loan[0]
            print("num_of_active_loan is ", num_of_active_loan)

            # check if the user is not having any unpaid fine
            cursor.execute("SELECT COUNT(fine_ID) FROM fine where user_ID = %s and paid=0", [user_ID])
            num_of_unpaid_fine = cursor.fetchone()
            num_of_unpaid_fine = num_of_unpaid_fine[0]
            print("num_of_unpaid_fine is: ", num_of_unpaid_fine)

            print("book_list//" + ISBN)

            # if user is in good condition, create loan details
            if ((num_of_active_loan < borrow_amount_limit) and (num_of_unpaid_fine == 0)):
                today = date.today()
                print(today)
                loan_due_date = today + timedelta(days=borrow_time_limit)
                print(loan_due_date)

                # get the available copies from the database
                cursor.execute("SELECT copy_ID FROM copy where item_ID = %s and loaned=0 and damaged=0 and lost=0", [ISBN])
                available_copies = dictfetchall(cursor)
                print("available_copies is: ", available_copies)
                copy_to_be_loaned = available_copies[0]
                copy_to_be_loaned = copy_to_be_loaned['copy_ID']
                print("copy_to_be_loaned is: ", copy_to_be_loaned)

                item_type = "book"

                # create loan details
                cursor.execute("INSERT INTO loan (user_ID, user_type_ID, item_ID, item_copy_ID, item_type, borrow_date, return_due_date, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [user_ID, user_type, ISBN, copy_to_be_loaned, item_type, today, loan_due_date, 1])
                row = cursor.fetchall()

                # change the status of the copy to “loaned: 1” in ‘copy’ table
                cursor.execute("UPDATE copy SET loaned=1 WHERE item_ID = %s and copy_ID = %s", [ISBN, copy_to_be_loaned])
                row = cursor.fetchall()

                messages.info(request, 'You have successfully borrowed this book. Check out My Account page for loan details.')
                context = {'book_detail': book_detail, 'num_of_copies_available': num_of_copies_available}
                return redirect("book_list//" + ISBN)
            else:
                messages.info(request, 'You have reached the borrow limit or currently have unpaid fines.')
                context = {'book_detail': book_detail, 'num_of_copies_available': num_of_copies_available}
                return redirect("book_list//" + ISBN)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]