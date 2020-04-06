from django.urls import path

from . import views

urlpatterns=[
    path('', views.laptop_list, name='laptop_list'),
    path('/<category>', views.laptop_list_by_category, name='laptop_list_by_category'),
    path('//<lap_model>', views.laptop_details_page, name='laptop_details_page'),
    path('logout', views.logout, name='logout'),
]