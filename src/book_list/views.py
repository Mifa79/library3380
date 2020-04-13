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
        # print(books.book.book_title)
        context = {'subjects': subjects, 'books': books, "category": category}
    return render(request, 'book_list.html', context)


def book_details_page(request, ISBN):
    print("Book ISBN is ", ISBN)
    with connection.cursor() as cursor:
        # get all the details of the book
        cursor.execute("SELECT ISBN, book_title, book_author, book_subject, book_publisher, date_of_publication, MSRP FROM book WHERE ISBN= %s", [ISBN])
        # cursor.execute("SELECT ISBN, book_title, book_author FROM book WHERE book_subject= %s", [category])

        book_details = dictfetchall(cursor)
        book_detail = book_details[0]
        # book_detail = cursor.fetchall()
        print("Book Details is: ", book_detail)
        # print(book_detail.book_title)
        context = {'book_detail': book_detail}
    return render(request, 'book_details.html', context)


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