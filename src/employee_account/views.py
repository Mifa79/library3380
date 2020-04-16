from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect

# Create your views here.
@login_required(login_url='/my_login')
def employeePage(request):
    user = request.user
    context = {'user': user}
    return render(request, 'employee_account.html', context)


@login_required(login_url='/my_login')
def manage_books(request):
    return render(request, 'manage_books.html')


@login_required(login_url='/my_login')
def manage_books_add(request):
    context = {'failedAdd':False}
    if request.method == 'POST':
        if request.POST.get('book_isbn') and request.POST.get('book_title') and request.POST.get('book_author') and request.POST.get('book_publisher') and request.POST.get('book_subject') and request.POST.get('book_date_of_publication') and request.POST.get('book_MSRP'):
            isbn = request.POST.get('book_isbn')
            title = request.POST.get('book_title')
            author = request.POST.get('book_author')
            pub = request.POST.get('book_publisher')
            sub = request.POST.get('book_subject')
            dop = request.POST.get('book_date_of_publication')
            msrp = request.POST.get('book_MSRP')
            with connection.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO book VALUES (%s, %s, %s, %s, %s, %s, %s)", [isbn, title, author, pub, sub, dop, msrp])
                except:
                    context = {'failedAdd':True}
                    print("Adding book unsuccessful, ISBN was not unique.")
                    pass
    return render(request, 'manage_books_add.html', context)

@login_required(login_url='/my_login')
def manage_books_delete(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM book")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    if request.method == 'POST':
        if request.POST.get('book-to-del-radio'):
            isbn = request.POST.get('book-to-del-radio')
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM book WHERE ISBN = %s", [isbn])
    return render(request, 'manage_books_delete.html', context)


@login_required(login_url='/my_login')
def manage_books_edit_select(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM book")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    if request.method == 'GET':
        if request.GET.get('book-to-edit-radio'):
            edit_isbn = request.GET.get('book-to-edit-radio')
            base_url = '/employeePage/manage_books/edit'
            new_url = base_url + '/' + str(edit_isbn)
            return redirect(new_url, isbn=edit_isbn)
    return render(request, 'manage_books_edit_select.html', context)


@login_required(login_url='/my_login')
def manage_books_edit(request, isbn):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM book WHERE ISBN = %s", [isbn])
        cols = cursor.fetchall()
        context = {'cols':cols}
    if request.method == 'POST':
        if request.POST.get('book_isbn') and request.POST.get('book_title') and request.POST.get('book_author') and request.POST.get('book_publisher') and request.POST.get('book_subject') and request.POST.get('book_date_of_publication') and request.POST.get('book_MSRP'):
            new_isbn = request.POST.get('book_isbn')
            title = request.POST.get('book_title')
            author = request.POST.get('book_author')
            pub = request.POST.get('book_publisher')
            sub = request.POST.get('book_subject')
            dop = request.POST.get('book_date_of_publication')
            msrp = request.POST.get('book_MSRP')
            with connection.cursor() as cursor:
                cursor.execute("UPDATE book SET ISBN = %s, book_title = %s, book_author = %s, book_publisher = %s, book_subject = %s, date_of_publication = %s, MSRP = %s WHERE ISBN = %s", [new_isbn, title, author, pub, sub, dop, msrp, isbn])
                return redirect(manage_books_edit_select)
    return render(request, 'manage_books_edit.html', context)


@login_required(login_url='/my_login')
def manage_books_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM book")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    return render(request, 'manage_books_list.html', context)


@login_required(login_url='/my_login')
def manage_laptops(request):
    return render(request, 'manage_laptops.html')


@login_required(login_url='/my_login')
def manage_laptops_add(request):
    context = {'failedAdd':False}
    if request.method == 'POST':
        if request.POST.get('lap_model'):
            model = request.POST.get('lap_model')
            os = request.POST.get('lap_OS')
            manu = request.POST.get('lap_manufacturer')
            with connection.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO laptop (lap_model, lap_OS, date_of_manufacture, MSRP, lap_manufacturer) VALUES (%s, %s, NULL, NULL, %s)", [model, os, manu])
                except:
                    context = {'failedAdd': True}
                    print("Adding laptop unsuccessful, laptop model was not unique.")
                    pass
                if request.POST.get('lap_date_of_manufacture'):
                    dom = request.POST.get('lap_date_of_manufacture')
                    cursor.execute("UPDATE laptop SET date_of_manufacture = %s WHERE lap_model = %s", [dom, model])
                if request.POST.get('lap_MSRP'):
                    MSRP = request.POST.get('lap_MSRP')
                    cursor.execute("UPDATE laptop SET MSRP = %s WHERE lap_model = %s", [MSRP, model])
    return render(request, 'manage_laptops_add.html', context)

@login_required(login_url='/my_login')
def manage_laptops_delete(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM laptop")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    if request.method == 'POST':
        if request.POST.get('lap-to-del-radio'):
            model = request.POST.get('lap-to-del-radio')
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM laptop WHERE lap_model = %s", [model])
    return render(request, 'manage_laptops_delete.html', context)


@login_required(login_url='/my_login')
def manage_laptops_edit_select(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM laptop")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    if request.method == 'GET':
        if request.GET.get('lap-to-edit-radio'):
            edit_model = request.GET.get('lap-to-edit-radio')
            base_url = '/employeePage/manage_laptops/edit'
            new_url = base_url + '/' + str(edit_model)
            return redirect(new_url, model=edit_model)
    return render(request, 'manage_laptops_edit_select.html', context)


@login_required(login_url='/my_login')
def manage_laptops_edit(request, model):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM laptop WHERE lap_model = %s", [model])
        cols = cursor.fetchall()
        context = {'cols':cols}
    if request.method == 'POST':
        if request.POST.get('lap_model'):
            new_model = request.POST.get('lap_model')
            os = request.POST.get('lap_OS')
            manu = request.POST.get('lap_manufacturer')
            lapAttrList = [new_model, os, manu, model]
            with connection.cursor() as cursor:
                cursor.execute("UPDATE laptop SET lap_model = %s, lap_OS = %s, date_of_manufacture = NULL, MSRP = NULL, lap_manufacturer = %s WHERE lap_model = %s", lapAttrList)
                if request.POST.get('lap_date_of_manufacture'):
                    dom = request.POST.get('lap_date_of_manufacture')
                    cursor.execute("UPDATE laptop SET date_of_manufacture = %s WHERE lap_model = %s", [dom, model])
                if request.POST.get('lap_MSRP'):
                    MSRP = request.POST.get('lap_MSRP')
                    cursor.execute("UPDATE laptop SET MSRP = %s WHERE lap_model = %s", [MSRP, model])
                return redirect(manage_laptops_edit_select)
    return render(request, 'manage_laptops_edit.html', context)


@login_required(login_url='/my_login')
def manage_laptops_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM laptop")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    return render(request, 'manage_laptops_list.html', context)


@login_required(login_url='/my_login')
def manage_media(request):
    return render(request, 'manage_media.html')


@login_required(login_url='/my_login')
def manage_media_add(request):
    context = {'failedAdd':False}
    if request.method == 'POST':
        if request.POST.get('media_id') and request.POST.get('media_title') and request.POST.get('media_author') and request.POST.get('media_publisher') and request.POST.get('media_subject') and request.POST.get('media_date_of_publication') and request.POST.get('media_MSRP'):
            id = request.POST.get('media_id')
            title = request.POST.get('media_title')
            author = request.POST.get('media_author')
            pub = request.POST.get('media_publisher')
            sub = request.POST.get('media_subject')
            dop = request.POST.get('media_date_of_publication')
            msrp = request.POST.get('media_MSRP')
            with connection.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO media VALUES (%s, %s, %s, %s, %s, %s, %s)", [id, title, author, pub, sub, dop, msrp])
                except:
                    context = {'failedAdd':True}
                    print("Adding media unsuccessful, ID was not unique.")
                    pass
    return render(request, 'manage_media_add.html', context)


@login_required(login_url='/my_login')
def manage_media_delete(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM media")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    if request.method == 'POST':
        if request.POST.get('media-to-del-radio'):
            id = request.POST.get('media-to-del-radio')
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM media WHERE media_ID = %s", [id])
    return render(request, 'manage_media_delete.html', context)


@login_required(login_url='/my_login')
def manage_media_edit_select(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM media")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    if request.method == 'GET':
        if request.GET.get('media-to-edit-radio'):
            edit_id = request.GET.get('media-to-edit-radio')
            base_url = '/employeePage/manage_media/edit'
            new_url = base_url + '/' + str(edit_id)
            return redirect(new_url, id=edit_id)
    return render(request, 'manage_media_edit_select.html', context)


@login_required(login_url='/my_login')
def manage_media_edit(request, id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM media WHERE media_ID = %s", [id])
        cols = cursor.fetchall()
        context = {'cols':cols}
    if request.method == 'POST':
        if request.POST.get('media_id') and request.POST.get('media_title') and request.POST.get(
                'media_author') and request.POST.get('media_publisher') and request.POST.get(
                'media_subject') and request.POST.get('media_date_of_publication') and request.POST.get('media_MSRP'):
            new_id = request.POST.get('media_id')
            title = request.POST.get('media_title')
            author = request.POST.get('media_author')
            pub = request.POST.get('media_publisher')
            sub = request.POST.get('media_subject')
            dop = request.POST.get('media_date_of_publication')
            msrp = request.POST.get('media_MSRP')
            with connection.cursor() as cursor:
                cursor.execute("UPDATE media SET media_ID = %s, media_title = %s, media_author = %s, media_publisher = %s, media_subject = %s, media_date_publication = %s, MSRP = %s WHERE media_ID = %s", [new_id, title, author, pub, sub, dop, msrp, id])
                return redirect(manage_media_edit_select)
    return render(request, 'manage_media_edit.html', context)


@login_required(login_url='/my_login')
def manage_media_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM media")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    return render(request, 'manage_media_list.html', context)


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