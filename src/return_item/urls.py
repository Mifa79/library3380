from django.urls import path

from . import views

urlpatterns=[
    path('', views.return_item, name='return_item'),
]