from django.urls import path

from . import views

urlpatterns=[
    path('', views.cart, name='cart'),
    path('logout', views.logout, name='logout'),
]