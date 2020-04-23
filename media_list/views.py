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
    print("media_ID is ", media_ID)
    with connection.cursor() as cursor:
        # get all the details of the media
        cursor.execute("SELECT media_ID, media_title, media_author, media_publisher, media_subject, media_date_publication, MSRP FROM media WHERE media_ID= %s", [media_ID])
        media_details = dictfetchall(cursor)
        media_detail = media_details[0]
        print("Media Details are: ", media_detail)

        # check number of available copies:
        cursor.execute("SELECT COUNT(copy_ID) FROM copy where item_ID= %s and loaned=0 and damaged=0 and lost=0", [media_ID])
        num_of_copies_available = cursor.fetchone()
        num_of_copies_available = num_of_copies_available[0]
        print("num_of_copies_available is: ", num_of_copies_available)

        context = {'media_detail': media_detail, 'num_of_copies_available': num_of_copies_available}
        return render(request, 'media_details.html', context)


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