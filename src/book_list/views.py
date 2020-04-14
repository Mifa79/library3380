from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required


def book_list(request):
    with connection.cursor() as cursor:
        # get all the book subjects
        cursor.execute("SELECT DISTINCT book_subject FROM book")
        subjects = [item[0] for item in cursor.fetchall()]
        # get all the books in database
        cursor.execute("SELECT ISBN, book_title, book_author FROM book")
        books = dictfetchall(cursor)
        context = {'subjects': subjects, 'books': books}
    return render(request, 'book_list.html', context)
    

def book_list_by_category(request, category):
    with connection.cursor() as cursor:
        # get all the book subjects
        cursor.execute("SELECT DISTINCT book_subject FROM book")
        subjects = [item[0] for item in cursor.fetchall()]
        # get all the books in a particular subject
        cursor.execute("SELECT ISBN, book_title, book_author FROM book WHERE book_subject= %s", [category])
        books = dictfetchall(cursor)
        # print("books are: ", books)
        context = {'subjects': subjects, 'books': books, "category": category}
    return render(request, 'book_list.html', context)


def book_details_page(request, ISBN):
    print("Book ISBN is ", ISBN)
    with connection.cursor() as cursor:
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

        context = {'book_detail': book_detail, 'num_of_copies_available': num_of_copies_available}
        return render(request, 'book_details.html', context)


# def borrow(request):
#     with connection.cursor() as cursor:
#         if request.method == "POST":
#             ISBN = request.POST['ISBN']
#              # get all the details of the book
#             cursor.execute("SELECT ISBN, book_title, book_author, book_subject, book_publisher, date_of_publication, MSRP FROM book WHERE ISBN= %s", [ISBN])
#             book_details = dictfetchall(cursor)
#             book_detail = book_details[0]
#             print("Book Details is: ", book_detail)

#             # check number of available copies:
#             cursor.execute("SELECT COUNT(copy_ID) FROM copy where item_ID= %s and loaned=0 and damaged=0 and lost=0", [ISBN])
#             num_of_copies_available = cursor.fetchone()
#             num_of_copies_available = num_of_copies_available[0]
#             print("num_of_copies_available is: ", num_of_copies_available)
            
#             user = request.user
#             print("user is: ", user)
#             if user is not None:
#                 # get user info from the database
#                 cursor.execute("SELECT id, user_type FROM sign_up_user WHERE username= %s", [user])
#                 user_info = dictfetchall(cursor)
#                 user_info = user_info[0]
#                 print ("user info is: ", user_info)
#                 print(user_info['id'])
#                 user_ID = user_info['id']
#                 print(user_info['user_type'])
#                 user_type = user_info['user_type']

#                 # get user type info from the database
#                 cursor.execute("SELECT borrow_time_limit, borrow_amount_limit, reservation_amount_limit FROM user_type_info WHERE user_type_ID= %s", [user_type])
#                 user_type_info = dictfetchall(cursor)
#                 user_type_info = user_type_info[0]
#                 print("user_type_info is: ", user_type_info)

#                 # count the number of active loan of the user
#                 cursor.execute("SELECT COUNT(loan_ID) FROM loan where user_ID = %s and active=0", [user_ID])
#                 num_of_active_loan = cursor.fetchone()
#                 num_of_active_loan = num_of_active_loan[0]
#                 print(num_of_active_loan)

#                 # check if the user is not having any unpaid fine
#                 cursor.execute("SELECT COUNT(fine_ID) FROM fine where user_ID = %s and paid=0", [user_ID])
#                 num_of_unpaid_fine = cursor.fetchone()
#                 num_of_unpaid_fine = num_of_unpaid_fine[0]
#                 print(num_of_unpaid_fine)

#             else: 
#                 messages.info(request, 'Please login to borrow or reserve book.')
#                 context = {'book_detail': book_detail, 'num_of_copies_available': num_of_copies_available}
#                 return render(request, 'book_details.html', context)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


@login_required
def logout(request):
    myLogout(request)
    return redirect('/')