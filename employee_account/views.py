from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required
from django.db import connection
from datetime import datetime, timedelta
import datetime
import json

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
def manage_books_add_copies(request):
    if request.method == 'POST':
        isbn = request.POST.get('book_isbn')
        num = request.POST.get('book_copy_num')
        count = 0
        with connection.cursor() as cursor:
            while (count < int(num)):
                count = count + 1
                cursor.execute("INSERT INTO copy (item_ID, loaned, damaged, lost, item_type) VALUES (%s, %s, %s, %s, %s)", [isbn, 0, 0, 0, "book"])

        return render(request, 'manage_books_add_copies.html')

    else:
        return render(request, 'manage_books_add_copies.html')


@login_required(login_url='/my_login')
def manage_laptops_add_copies(request):
    if request.method == 'POST':
        lap_model = request.POST.get('lap_model')
        num = request.POST.get('laptop_copy_num')
        count = 0
        with connection.cursor() as cursor:
            while (count < int(num)):
                count = count + 1
                cursor.execute("INSERT INTO copy (item_ID, loaned, damaged, lost, item_type) VALUES (%s, %s, %s, %s, %s)", [lap_model, 0, 0, 0, "laptop"])

        return render(request, 'manage_laptops_add_copies.html')

    else:
        return render(request, 'manage_laptops_add_copies.html')


@login_required(login_url='/my_login')
def manage_media_add_copies(request):
    if request.method == 'POST':
        media_ID = request.POST.get('media_ID')
        num = request.POST.get('media_copy_num')
        count = 0
        with connection.cursor() as cursor:
            while (count < int(num)):
                count = count + 1
                cursor.execute("INSERT INTO copy (item_ID, loaned, damaged, lost, item_type) VALUES (%s, %s, %s, %s, %s)", [media_ID, 0, 0, 0, "media"])

        return render(request, 'manage_media_add_copies.html')

    else:
        return render(request, 'manage_media_add_copies.html')



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
        elif request.POST.get('LoanResultsAll'):
            return redirect('/employeePage/reports/LoanResults/')
        elif request.POST.get('SubjectAmounts'):
            return redirect('/employeePage/reports/SubjectAmounts/')

    return render(request, 'report_select.html')
    # If statement for POST for report type
        # Any if statements for report date ranges or other options



@login_required(login_url='/my_login')
def UserSignupDateGraphWeek(request):
    days = []
    date = datetime.datetime.now()
    i = 7
    while i >= 0:
        day = datetime.datetime(date.year, date.month, date.day - i)
        days.append(day.strftime('%x'))
        i -= 1
    categories = days
    print("CATEGORIES", categories)
    with connection.cursor() as cursor:
        try:
            userCount = []
            userInfo = []
            dateDate = datetime.date.today()
            for i in range(7, -1, -1):
                day = dateDate - timedelta(days = i)
                print(day)
                cursor.execute("SELECT COUNT(*) FROM sign_up_user WHERE CAST(date_joined AS DATE) = %s", [day])
                result = cursor.fetchall()
                if result[0][0] > 0:
                    """SELECTING USER INFO FOR TABLE WHERE NECESSARY"""
                    cursor.execute("SELECT username, first_name, last_name, user_type, CAST(date_joined AS DATE) FROM sign_up_user WHERE CAST(date_joined AS DATE) = %s", [day])
                    userInfo.append(cursor.fetchall())
                else:
                    userInfo.append(0)
                print("RESULT:", result, "RESULT[0]", result[0][0])
                userCount.append(result[0][0])
            userInfoCols = ['Username', 'First Name', 'Last Name', 'User Type', 'Date Joined']
            print("USERCOUNT:", userCount)
            print("USERINFO:", userInfo)
        except:
            print("FAILED USERDATA QUERY")
            return(redirect(report_select))

        # REFERENCE: https://www.highcharts.com/demo/column-basic
        """CREATING HIGHCHART"""
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
    return render(request, 'UserSignupDateGraphWeek.html', {'chart': dump, 'userInfo': userInfo, 'userInfoCols': userInfoCols})



@login_required(login_url='/my_login')
def UserSignupDateGraphMonth(request):
    # TODO: Add Label for Dates (x-axis label)
    days = []
    date = datetime.datetime.now()
    i = 31
    while i >= 0:
        day = date - timedelta(days=i)
        days.append(day.strftime('%x'))
        i -= 1
    categories = days
    print("CATEGORIES", categories)
    with connection.cursor() as cursor:
        try:
            userCount = []
            userInfo = []
            
            dateDate = datetime.date.today()
            for i in range(31, -1, -1):
                day = dateDate - timedelta(days=i)
                print(day)
                cursor.execute("SELECT COUNT(*) FROM sign_up_user WHERE CAST(date_joined AS DATE) = %s", [day])
                result = cursor.fetchall()
                if result[0][0] > 0:
                    """SELECTING USER INFO FOR TABLE WHERE NECESSARY"""
                    cursor.execute("SELECT username, first_name, last_name, user_type, CAST(date_joined AS DATE) FROM sign_up_user WHERE CAST(date_joined AS DATE) = %s", [day])
                    userInfo.append(cursor.fetchall())
                    
                else:
                    userInfo.append(0)
                print("RESULT:", result, "RESULT[0]", result[0][0])
                userCount.append(result[0][0])
            print("USERCOUNT:", userCount)
            userInfoCols = ['Username', 'First Name', 'Last Name', 'User Type', 'Date Joined']
            print("USERINFO:", userInfo)
        except:
            print("FAILED USERDATA QUERY")
            return(redirect(report_select))

        """CREATING HIGHCHART"""
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
            """FETCHING COUNTS OF LOANS BY RESULT"""
            # Total Loans
            cursor.execute("SELECT COUNT(*) FROM loan")
            totalLoans = cursor.fetchall()
            if totalLoans[0][0] or totalLoans[0][0] == 0:
                totalLoans = totalLoans[0][0]
            else: totalLoans = 0
            
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
            if lostLoans[0][0] or lostLoans[0][0] == 0:
                lostLoans = lostLoans[0][0]
            else: lostLoans = 0
            print("LOST:",lostLoans)
            # Active Loans
            cursor.execute("SELECT COUNT(*) FROM loan WHERE active = 1")
            activeLoans = cursor.fetchall()
            print("ACTIVE:",activeLoans)
            if activeLoans[0][0] or activeLoans[0][0] == 0:
                activeLoans = activeLoans[0][0]
            else: activeLoans = 0

            returnedLoans = totalLoans - overdueLoans - damagedLoans - activeLoans - lostLoans

            """QUERYING FOR DATA FOR EACH TABLE BY RESULT"""
            infoCols = ["Loan ID", "User ID", "User Type ID", "Item ID", "Item Copy ID", "Item Type", "Borrow Date", "Return Due Date"]
            query = "SELECT loan_ID, user_ID, user_type_ID, item_ID, item_copy_ID, item_type, borrow_date, return_due_date FROM loan WHERE "
            cursor.execute(query + "overdue_date_num > 0")
            overdueLoanInfo = cursor.fetchall()
            cursor.execute(query + "damaged = 1")
            damagedLoanInfo = cursor.fetchall()
            cursor.execute(query + "lost = 1")
            lostLoanInfo = cursor.fetchall()
            cursor.execute(query + "active = 1")
            activeLoanInfo = cursor.fetchall()
            cursor.execute(query + "overdue_date_num = 0 AND damaged = 0 AND lost = 0 AND active = 0")
            returnedLoanInfo = cursor.fetchall()

            """CREATING HIGHCHART"""

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
                            'format': '<b>{point.name}</b>: {point.percentage:.1f}%'
                        }
                    }
                },
                'series': myseries
            }
            dump = json.dumps(chart)
            print(dump)
            return render(request, 'loanResults.html', {'chart': dump, 'totalLoans': totalLoans, 'infoCols': infoCols, 'overdueLoanInfo': overdueLoanInfo, 'damagedLoanInfo': damagedLoanInfo, 'lostLoanInfo': lostLoanInfo, 'activeLoanInfo': activeLoanInfo, 'returnedLoanInfo': returnedLoanInfo})

        except:
            print("FAILED LOAN QUERY")
            return redirect(report_select)



@login_required(login_url='/my_login')
def subjectAmounts(request):
    with connection.cursor() as cursor:
        bsubs = []  # Book Subjects
        msubs = []  # Media Subjects
        cursor.execute("SELECT DISTINCT book_subject FROM book")
        fetch = cursor.fetchall()
        print("DISTINCT BOOK SUBJECTS:", fetch)
        for bSub in fetch:
            bsubs.append(bSub[0])
        cursor.execute("SELECT DISTINCT media_subject FROM media")
        fetch = cursor.fetchall()
        print("DISTINCT MEDIA SUBJECTS:", fetch)
        for mSub in fetch:
            msubs.append(mSub[0])
        print(bsubs, msubs)
        subjects = list(set(bsubs).symmetric_difference(set(msubs)))
        subjects += list(set(bsubs).intersection(set(msubs)))
        print("SUBJECTS:", subjects)

        """QUERY FOR COUNT DATA"""
        bookCounts = []  # Indices of these two lists should align with subjects list
        mediaCounts = []
        for subject in subjects:
            cursor.execute("SELECT COUNT(*) FROM book WHERE book_subject = %s", [subject])
            bCount = cursor.fetchall()
            if bCount[0][0] or bCount[0][0] == 0:
                bCount = bCount[0][0]
            else:
                bCount = 0
            bookCounts.append(bCount)
            cursor.execute("SELECT COUNT(*) FROM media WHERE media_subject = %s", [subject])
            mCount = cursor.fetchall()
            if mCount[0][0] or mCount[0][0] == 0:
                mCount = mCount[0][0]
            else:
                mCount = 0
            mediaCounts.append(mCount)

    """QUERYING FOR DATA FOR EACH TABLE BY RESULT"""
    infoCols = ["Subject", "Asset Type", "Primary Key Value", "Title", "Author", "Publisher", "Date of Publication", "Total Number of Copies", "MSRP"]
    tables = []
    for subject in subjects:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT book_subject, 'Book' AS tablename, ISBN, book_title, book_author, book_publisher, date_of_publication, total_copy_num, MSRP FROM book WHERE book_subject = %s", [subject])
                books = cursor.fetchall()
                cursor.execute("SELECT media_subject, 'Media' AS tablename, media_ID, media_title, media_author, media_publisher, media_date_publication, total_copy_num, MSRP FROM media WHERE media_subject = %s", [subject])
                media = cursor.fetchall()
                myList = books + media
                tables.append(myList)
        except:
            print("SUBJECT QUERY FAILED")

    """MISC DATA GATHERING"""
    # Total books int
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM book")
        count = cursor.fetchall()
        totalBooks = count[0][0]
        # Total media int
        cursor.execute("SELECT COUNT(*) FROM media")
        count = cursor.fetchall()
        totalMedia = count[0][0]
    # Total subjects int
    totalSubjects = len(subjects)

    # REFERENCE: https://www.highcharts.com/demo/column-basic
    """CREATING HIGHCHART"""
    myseries = [
        {
            'name': 'Books',
            'data': bookCounts
        },
        {
            'name': 'Media',
            'data': mediaCounts
        }
    ]
    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Book and Media Count by Subject'},
        'xAxis': {'categories': subjects, 'title': {'text': 'Subjects'}},
        'yAxis': {
            'min': 0,
            'title': {
                'text': 'Amount',
                'align': 'high'
            }
        },
        'series': myseries
    }
    dump = json.dumps(chart)
    return render(request, 'subjectAmounts.html', {'chart': dump, 'infoCols': infoCols, 'subjects': subjects, 'tables': tables, 'totalBooks': totalBooks, 'totalMedia': totalMedia, 'totalSubjects': totalSubjects})





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