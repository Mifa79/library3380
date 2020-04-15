from django.urls import path

from . import views

urlpatterns=[
    path('', views.pay_fine, name='pay_fine'),
]