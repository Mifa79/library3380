from django.urls import path

from . import views

urlpatterns=[
    path('', views.myLogin, name='my_login'),
    # path('login',views.login,name='login'),
    # # path('',views.account,name='account'),
    path('/accountPage', views.accountPage,name='accountPage'),
    path('/employeePage', views.employeePage,name='employeePage'),
]