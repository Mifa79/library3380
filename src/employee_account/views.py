from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
import datetime
import json

# Create your views here.
@login_required
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
            num = request.POST.get('book_total_copy_num')
            with connection.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO book VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [isbn, title, author, pub, sub, dop, msrp, num])
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
            print(edit_isbn)
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
            num = request.POST.get('book_total_copy_num')
            with connection.cursor() as cursor:
                cursor.execute("UPDATE book SET ISBN = %s, book_title = %s, book_author = %s, book_publisher = %s, book_subject = %s, date_of_publication = %s, MSRP = %s, total_copy_num = %s WHERE ISBN = %s", [new_isbn, title, author, pub, sub, dop, msrp, num, isbn])
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
        if request.POST.get('lap_model') and request.POST.get('lap_OS') and request.POST.get('lap_manufacturer'):
            model = request.POST.get('lap_model')
            os = request.POST.get('lap_OS')
            manu = request.POST.get('lap_manufacturer')
            num = request.POST.get('lap_total_num_copies')
            with connection.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO laptop (lap_model, lap_OS, date_of_manufacture, MSRP, lap_manufacturer, total_copy_num) VALUES (%s, %s, NULL, NULL, %s, %s)", [model, os, manu, num])
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
            num = request.POST.get('lap_total_copy_num')
            lapAttrList = [new_model, os, manu, num, model]
            with connection.cursor() as cursor:
                cursor.execute("UPDATE laptop SET lap_model = %s, lap_OS = %s, date_of_manufacture = NULL, MSRP = NULL, lap_manufacturer = %s, total_copy_num = %s WHERE lap_model = %s", lapAttrList)
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
            num = request.POST.get('media_total_copy_num')
            with connection.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO media VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [id, title, author, pub, sub, dop, msrp, num])
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
            num = request.POST.get('media_total_copy_num')
            with connection.cursor() as cursor:
                cursor.execute("UPDATE media SET media_ID = %s, media_title = %s, media_author = %s, media_publisher = %s, media_subject = %s, media_date_publication = %s, MSRP = %s, total_copy_num = %s WHERE media_ID = %s", [new_id, title, author, pub, sub, dop, msrp, num, id])
                return redirect(manage_media_edit_select)
    return render(request, 'manage_media_edit.html', context)


@login_required(login_url='/my_login')
def manage_media_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM media")
        tableRows = cursor.fetchall()
        context = {'tableRows':tableRows}
    return render(request, 'manage_media_list.html', context)


@login_required(login_url='/my_login')
def manage_list_all(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM book")
        bookRows = cursor.fetchall()
        bookCols = [col[0] for col in cursor.description]
        cursor.execute("SELECT * FROM laptop")
        lapRows = cursor.fetchall()
        lapCols = [col[0] for col in cursor.description]
        cursor.execute("SELECT * FROM media")
        mediaRows = cursor.fetchall()
        mediaCols = [col[0] for col in cursor.description]
        context = {'bookRows':bookRows, 'bookCols':bookCols, 'lapRows':lapRows, 'lapCols':lapCols, 'mediaRows':mediaRows, 'mediaCols':mediaCols}
    return render(request, 'manage_list_all.html', context)

@login_required(login_url='/my_login')
def report_select(request):
    if request.method == 'POST':
        if request.POST.get('UserSignupsGraphWeek'):
            return redirect('/employeePage/reports/UserSignupsGraphWeek/')
        elif request.POST.get('UserSignupsGraphMonth'):
            return redirect('/employeePage/reports/UserSignupsGraphMonth/')
        elif request.POST.get('LoanResults'):
            return redirect('/employeePage/reports/LoanResults/')
    return render(request, 'report_select.html')
    # If statement for POST for report type
        # Any if statements for report date ranges or other options

@login_required(login_url='/my_login')
def UserSignupDateGraphWeek(request):
    days = []
    date = datetime.datetime.now()
    for i in range(7, 0, -1):
        day = datetime.datetime(date.year, date.month, date.day - i)
        days.append(day.strftime('%x'))
    days.append(date.strftime('%x'))
    categories = days
    print("CATEGORIES", categories)
    with connection.cursor() as cursor:
        try:
            userCount = []
            userInfo = []
            userInfoCols = []
            date = datetime.datetime.now()
            for i in range(7):
                day = datetime.datetime(date.year, date.month, date.day - i)
                print(day)
                cursor.execute("SELECT COUNT(*) FROM sign_up_user WHERE CAST(date_joined AS DATE) = %s", [day])
                result = cursor.fetchall()
                if result[0][0] > 0:
                    cursor.execute("SELECT username, first_name, last_name, user_type, CAST(date_joined AS DATE) FROM sign_up_user WHERE CAST(date_joined AS DATE) = %s", [day])
                    userInfo.append(cursor.fetchall())
                    userInfoCols = [col[0] for col in cursor.description]
                else:
                    userInfo.append(0)
                print("RESULT:", result, "RESULT[0]", result[0][0])
                userCount.append(result[0][0])
            print("USERCOUNT:", userCount)
            print("USERINFO:", userInfo)
        except:
            print("FAILED USERDATA QUERY")
        myseries = [{
                'name': 'Users',
                'data': userCount
        }]
    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'User Signup Count (Past Week)'},
        'xAxis': {'categories': categories, 'title': {'text': 'Join Dates'}},
        'yAxis': {
            'min': 0,
            'title': {
                'text': 'Number of Users Joined',
                'align': 'high'
            }
        },
        'series': myseries
    }
    dump = json.dumps(chart)
    print(dump)
    return render(request, 'UserSignupDateGraphWeek.html', {'chart': dump, 'userInfo': userInfo, 'userInfoCols': userInfoCols})
    #     myseries = [{
    #             'name': 'Users',
    #             'data': userCount,
    #             'color': '#3771c8'
    #     }]
    #     chart = {'type': 'column'}
    #     title = {'text': 'User Signup Count (Past Week)'}
    #     subtitle = 'my subtitle'
    #     xAxis = {'categories': categories},
    #     yAxis = {
    #         'min': 0,
    #         'title': {
    #             'text': 'Number of Users Joined',
    #             'align': 'high'
    #         }
    #     }
    #     series = myseries,
    #     tooltip = {'shared': 'true',
    #                 'valueSuffix': 'users'},
    #     plot_options = {
    #         'bar': {
    #             'dataLabels': {
    #                 'enabled': 'true'
    #             }
    #         }
    #     }
    #     legend = {'layout': 'vertical', 'align': 'right',
    #                'floating': 'true', 'verticalAlign': 'top',
    #                'x': -40, 'borderWidth': 1,
    #                'y': -80, 'borderColor': '#e3e3e3'}
    #     chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    #     title = {"text": 'Check Valve Data'}
    #     xAxis = {"title": {"text": 'Serial Number'}, "categories": data['serial numbers']}
    #     yAxis = {"title": {"text": 'Data'}}
    #     series = [
    #         {"name": 'Mass (kg)', "data": data['mass']},
    #         {"name": 'Pressure Drop (psid)', "data": data['pressure drop']},
    #         {"name": 'Cracking Pressure (psid)', "data": data['cracking pressure']}
    #     ]
    #
    #     return render(request, 'unit/data_plot.html', {'chartID': chartID, 'chart': chart,
    #                                                    'series': series, 'title': title,
    #                                                    'xAxis': xAxis, 'yAxis': yAxis})
    # return render(request, 'UserSignupDateGraphWeek.html', {'chart': dump})
    # print(chart, plot_options, series, title, subtitle, tooltip, legend, xAxis, yAxis)
    # return render(request, 'UserSignupDateGraphWeek.html', {'chart': chart, 'plot_options': plot_options,
    #                             'series': series, 'title': title, 'subtitle': subtitle, 'tooltip': tooltip,
    #                             'legend': legend, 'xAxis': xAxis, 'yAxis': yAxis})

@login_required(login_url='/my_login')
def UserSignupDateGraphMonth(request):
    # TODO: Add Label for Dates (x-axis label)
    days = []
    date = datetime.datetime.now()
    for i in range(31, 1, -1):
        day = date - timedelta(days=i)
        days.append(day.strftime('%x'))
    days.append(date.strftime('%x'))
    categories = days
    print("CATEGORIES", categories)
    with connection.cursor() as cursor:
        try:
            userCount = []
            userInfo = []
            userInfoCols = []
            dateDate = datetime.date.today()
            for i in range(31):
                day = dateDate - timedelta(days=i)
                print(day)
                cursor.execute("SELECT COUNT(*) FROM sign_up_user WHERE CAST(date_joined AS DATE) = %s", [day])
                result = cursor.fetchall()
                if result[0][0] > 0:
                    cursor.execute("SELECT username, first_name, last_name, user_type, CAST(date_joined AS DATE) FROM sign_up_user WHERE CAST(date_joined AS DATE) = %s", [day])
                    userInfo.append(cursor.fetchall())
                    userInfoCols = [col[0] for col in cursor.description]
                else:
                    userInfo.append(0)
                print("RESULT:", result, "RESULT[0]", result[0][0])
                userCount.append(result[0][0])
            print("USERCOUNT:", userCount)
            print("USERINFO:", userInfo)
        except:
            print("FAILED USERDATA QUERY")
        myseries = [{
                'name': 'Users',
                'data': userCount
        }]
    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'User Signup Count (Past Month)'},
        'xAxis': {'categories': categories, 'title': {'text': 'Join Dates'}},
        'yAxis': {
            'min': 0,
            'title': {
                'text': 'Number of Users Joined',
                'align': 'high'
            }
        },
        'series': myseries
    }
    dump = json.dumps(chart)
    print(dump)
    return render(request, 'UserSignupDateGraphMonth.html', {'chart': dump, 'userInfo': userInfo, 'userInfoCols': userInfoCols})

@login_required(login_url='/my_login')
def loanResults(request):
    with connection.cursor() as cursor:
        try:
            totalLoans = None
            overdueLoans = None
            damagedLoans = None
            lostLoans = None
            activeLoans = None
            # Total Loans
            cursor.execute("SELECT COUNT(*) FROM loan")
            totalLoans = cursor.fetchall()
            if totalLoans[0][0] or totalLoans[0][0] == 0:
                totalLoans = totalLoans[0][0]
            else: totalLoans = 0
            print("TOTAL:",totalLoans)
            # Overdue Loans
            cursor.execute("SELECT COUNT(*) FROM loan WHERE overdue_date_num > 0")
            overdueLoans = cursor.fetchall()
            if overdueLoans[0][0] or overdueLoans[0][0] == 0:
                overdueLoans = overdueLoans[0][0]
            else: overdueLoans = 0
            print("OVERDUE:",overdueLoans)
            # Damaged Loans
            cursor.execute("SELECT COUNT(*) FROM loan WHERE damaged = 1")
            damagedLoans = cursor.fetchall()
            if damagedLoans[0][0] or damagedLoans[0][0] == 0:
                damagedLoans = damagedLoans[0][0]
            else: damagedLoans = 0
            print("DAMAGED:",damagedLoans)
            # Lost Loans
            cursor.execute("SELECT COUNT(*) FROM loan WHERE lost = 1")
            lostLoans = cursor.fetchall()
            if lostLoans is not None:
                lostLoans = lostLoans[0][0]
            else: lostLoans = 0
            print("LOST:",lostLoans)
            # Active Loans
            cursor.execute("SELECT COUNT(*) FROM loan WHERE active = 1")
            activeLoans = cursor.fetchall()
            print("ACTIVE:",activeLoans)
            if activeLoans[0][0] or activeLoans[0][0] == 0:
                activeLoans = activeLoans[0][0]
            else:
                activeLoans = 0
            returnedLoans = totalLoans - overdueLoans - damagedLoans - activeLoans - lostLoans
            myseries = [{
                'name': 'Loans',
                'colorByPoint': 'true',
                'data': [{
                    'name': 'Overdue',
                    'y': overdueLoans,
                    'sliced': 'true',
                    'selected': 'true'
                }, {
                    'name': 'Damaged',
                    'y': damagedLoans
                }, {
                    'name': 'Lost',
                    'y': lostLoans
                }, {
                    'name': 'Active',
                    'y': activeLoans
                }, {
                    'name': 'Returned Properly',
                    'y': returnedLoans
                }]
            }]
            chart = {
                'chart': {
                    # 'plotBackgroundColor': 'null',
                    # 'plotBorderWidth': 'null',
                    # 'plotShadow': 'false',
                    'type': 'pie'
                },
                'title': {'text': 'Loan Data'},
                'toolTip': {
                    'pointFormat': '{series.name}: <b>{point.percentage:.1f}</b>'
                },
                'plotOptions': {
                    'pie': {
                        'allowPointSelect': 'true',
                        'cursor': 'pointer',
                        'dataLabels': {
                            'enabled': 'true',
                            'format': '<b>{point.name}</b>: {point.percentage:.1f}'
                        }
                    }
                },
                'series': myseries
            }
            dump = json.dumps(chart)
            print(dump)
            return render(request, 'loanResults.html', {'chart': dump})
        except:
            print("FAILED LOAN QUERY")
            return redirect(report_select)

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