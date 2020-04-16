from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required


def laptop_list(request):
    with connection.cursor() as cursor:
        # get all the laptop_OS
        cursor.execute("SELECT DISTINCT lap_OS FROM laptop")
        lap_OSs = [item[0] for item in cursor.fetchall()]
        # get all the laptops in database
        cursor.execute("SELECT lap_model, lap_OS, lap_manufacturer FROM laptop")
        laptops = dictfetchall(cursor)
        context = {'lap_OSs': lap_OSs, 'laptops': laptops}
    return render(request, 'laptop_list.html', context)
    

def laptop_list_by_category(request, category):
    with connection.cursor() as cursor:
        # get all the laptop_OS
        cursor.execute("SELECT DISTINCT lap_OS FROM laptop")
        lap_OSs = [item[0] for item in cursor.fetchall()]
        # get all the laptops in a particular OS type
        cursor.execute("SELECT lap_model, lap_OS, lap_manufacturer FROM laptop WHERE lap_OS= %s", [category])
        laptops = dictfetchall(cursor)
        context = {'lap_OSs': lap_OSs, 'laptops': laptops, "category": category}
    return render(request, 'laptop_list.html', context)


Laptop detail def laptop_details_page(request, lap_model):
    print("Laptop model is ", lap_model)
    with connection.cursor() as cursor:
        # get all the details of the laptop
        cursor.execute("SELECT lap_model, lap_OS, date_of_manufacture, MSRP, lap_manufacturer FROM laptop WHERE lap_model= %s", [lap_model])
        laptop_details = dictfetchall(cursor)
        laptop_detail = laptop_details[0]
        print("Laptop Details is: ", laptop_detail)
        
        # check number of available copies:
        cursor.execute("SELECT COUNT(copy_ID) FROM copy where item_ID= %s and loaned=0 and damaged=0 and lost=0", [lap_model])
        num_of_copies_available = cursor.fetchone()
        num_of_copies_available = num_of_copies_available[0]
        print("num_of_copies_available is: ", num_of_copies_available)
        
        context = {'laptop_detail': laptop_detail, 'num_of_copies_available': num_of_copies_available}
    return render(request, 'laptop_details.html', context)


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
