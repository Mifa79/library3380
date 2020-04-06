from django.urls import path

from . import views

urlpatterns=[
    path('', views.userAccount,name='userAccount'),
    path('logout', views.logout, name='logout'),
]