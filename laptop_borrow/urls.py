from django.urls import path

from . import views

urlpatterns=[
    path('', views.laptop_borrow, name='laptop_borrow'),
]
