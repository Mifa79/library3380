from django.urls import path

from . import views

urlpatterns=[
    path('', views.employeePage,name='employeePage'),
    path('logout', views.logout, name='logout'),
]