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
        cursor.execute("SELECT book_title, book_author FROM book")
        books = dictfetchall(cursor)
        context = {'subjects': subjects, 'books': books}
    return render(request, 'book_list.html', context)
    

def book_list_by_category(request, category):
    print(category)
    with connection.cursor() as cursor:
        # get all the book subjects
        cursor.execute("SELECT DISTINCT book_subject FROM book")
        subjects = [item[0] for item in cursor.fetchall()]
        print(subjects)
        # get all the books in a particular subject
        cursor.execute("SELECT book_title, book_author FROM book WHERE book_subject= %s", [category])
        books = dictfetchall(cursor)
        print(books)
        context = {'subjects': subjects, 'books': books, "category": category}
    return render(request, 'book_list.html', context)

# def list_all_books(request):
#     with connection.cursor() as cursor:
#         print("hello")
#         cursor.execute("SELECT * FROM book")
#         row = cursor.fetchall()
#     return row
#     print(row)

# def add_book(request):
#     with connection.cursor() as cursor:
#         print("hello")
#         # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
#         # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
#         # row = cursor.fetchone()

#         cursor.execute("INSERT INTO book_all_copies VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ["1250313074", "Ninth House", "Alex Stern", "Fantasy", 16.78, "02", 0, 0, 0, "loan_01"])
#         row = cursor.fetchall()
#     return row

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