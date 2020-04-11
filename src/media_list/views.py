from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import logout as myLogout
from django.contrib.auth.decorators import login_required


def media_list(request):
    with connection.cursor() as cursor:
        # get all the media subjects
        cursor.execute("SELECT DISTINCT media_subject FROM media")
        subjects = [item[0] for item in cursor.fetchall()]
        # get all the medias in database
        cursor.execute("SELECT media_ID, media_title, media_author FROM media")
        medias = dictfetchall(cursor)
        context = {'subjects': subjects, 'medias': medias}
    return render(request, 'media_list.html', context)
    

def media_list_by_category(request, category):
    with connection.cursor() as cursor:
        # get all the media subjects
        cursor.execute("SELECT DISTINCT media_subject FROM media")
        subjects = [item[0] for item in cursor.fetchall()]
        # get all the medias in a particular subject
        cursor.execute("SELECT media_ID, media_title, media_author FROM media WHERE media_subject= %s", [category])
        medias = dictfetchall(cursor)
        context = {'subjects': subjects, 'medias': medias, "category": category}
    return render(request, 'media_list.html', context)


def media_details_page(request, media_ID):
    print("Media ID is ", media_ID)
    return render(request, 'media_details.html')


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