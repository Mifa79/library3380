from django.urls import path

from . import views

urlpatterns=[
    path('', views.media_borrow, name='media_borrow'),
]
