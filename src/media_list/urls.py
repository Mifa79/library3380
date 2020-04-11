from django.urls import path

from . import views

urlpatterns=[
    path('', views.media_list, name='media_list'),
    path('/<category>', views.media_list_by_category, name='media_list_by_category'),
    path('//<media_ID>', views.media_details_page, name='media_details_page'),
    path('logout', views.logout, name='logout'),
]