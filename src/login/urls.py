from django.urls import path

from . import views

urlpatterns=[
    path('', views.login, name='login'),
    # path('login',views.login,name='login'),
    # # path('',views.account,name='account'),
    # path('accountPage',views.accountPage,name='account page')
]