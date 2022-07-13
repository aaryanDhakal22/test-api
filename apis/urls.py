from django.urls import path

from .views import *

urlpatterns = [
    path('student/',student_list, name="student_list"),
    path('student/details/<str:unid>',student_detail,name="student_detail"),
    path('transaction/<str:unid>',transaction_list,name='transaction_list'),
    # path('transaction/details/<str:date>',transaction_detail,name='transaction_list'),

]
