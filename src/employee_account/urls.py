from django.urls import path

from . import views

urlpatterns=[
    path('', views.employeePage, name='employeePage'),
    path('/manage_books', views.manage_books, name='manage_books'),
    path('/manage_books/add/', views.manage_books_add, name='manage_books_add'),
    path('/manage_books/delete/', views.manage_books_delete, name='manage_books_delete'),
    path('/manage_books/edit/<isbn>', views.manage_books_edit, name='manage_books_edit'),
    path('/manage_books/edit_select/', views.manage_books_edit_select, name='manage_books_edit_select'),
    path('/manage_books/list/', views.manage_books_list, name="manage_books_list"),
    path('/manage_laptops', views.manage_laptops, name='manage_laptops'),
    path('/manage_laptops/add/', views.manage_laptops_add, name='manage_laptops_add'),
    path('/manage_laptops/delete/', views.manage_laptops_delete, name='manage_laptops_delete'),
    path('/manage_laptops/edit/<model>', views.manage_laptops_edit, name="manage_laptops_edit"),
    path('/manage_laptops/edit_select/', views.manage_laptops_edit_select, name='manage_laptops_edit_select'),
    path('/manage_laptops/list/', views.manage_laptops_list, name='manage_laptops_list'),
    path('/manage_media/', views.manage_media, name='manage_media'),
    path('/manage_media/add/', views.manage_media_add, name='manage_media_add'),
    path('/manage_media/delete/', views.manage_media_delete, name='manage_media_delete'),
    path('/manage_media/edit/<id>/', views.manage_media_edit, name='manage_media_edit'),
    path('/manage_media/edit_select/', views.manage_media_edit_select, name='manage_media_edit_select'),
    path('/manage_media/list/', views.manage_media_list, name='manage_media_list'),
    path('/manage/list_all/', views.manage_list_all, name='manage_list_all'),
    path('/reports/', views.report_select, name='report_select'),
    path('/reports/UserSignupsGraphWeek/', views.UserSignupDateGraphWeek, name='UserSignupDateGraphWeek'),
    path('/reports/UserSignupsGraphMonth/', views.UserSignupDateGraphMonth, name='UserSignupDateGraphMonth'),
    path('/reports/LoanResults/', views.loanResults, name='LoanResults'),
    path('/reports/SubjectAmounts/', views.subjectAmounts, name='SubjectAmounts'),
    path('logout', views.logout, name='logout')
]