from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('logout', views.logout, name='logout'),
    # path('account_page',views.login,name='account'),
    # path('accountPage',views.accountPage,name='account page')
]