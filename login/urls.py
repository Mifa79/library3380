from django.urls import path

from . import views

urlpatterns=[
    path('', views.myLogin, name='my_login'),
    path('/accountPage', views.accountPage,name='accountPage'),
    path('/employeePage', views.employeePage,name='employeePage'),
]