from django.urls import path

from sope import views 

urlpatterns = [

    path('',views.home, name = 'home'),
    path('createEmployee',views.createEmployee, name = 'create'),
    path('editEmployee<str:pk>',views.EditEmployee, name = 'edit'),
    path('employeeList', views.EmployeeList, name = 'list'),

]