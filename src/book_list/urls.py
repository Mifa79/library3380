from django.urls import path

from . import views

urlpatterns=[
    path('', views.book_list, name='book_list'),
    path('/<category>', views.book_list_by_category, name='book_list_by_category'),
]