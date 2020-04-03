from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    # # path('',views.account,name='account'),
    # path('accountPage',views.accountPage,name='account page')
]