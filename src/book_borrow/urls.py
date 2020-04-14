from django.urls import path

from . import views

urlpatterns=[
    path('', views.book_borrow, name='book_borrow'),
]