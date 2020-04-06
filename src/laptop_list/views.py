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


def laptop_details_page(request, lap_model):
    print("Laptop model is ", lap_model)
    return render(request, 'laptop_details.html')


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