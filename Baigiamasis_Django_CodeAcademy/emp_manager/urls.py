from django.urls import path
from . import views
from .views import base_view

urlpatterns = [
    path('', views.index, name='index'),
    path('all_emp', views.all_employees, name='all_emp'),
    path('add_emp', views.add_employee, name='add_emp'),
    path('remove_emp', views.remove_employee, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_employee, name='remove_emp'),
    path('filter_emp', views.filter_employee, name='filter_emp'),
    path('update_emp/<int:emp_id>', views.update_employee, name='update_emp'),
    path('update_emp', views.update_employee, name='update_emp'),
    path('base/', base_view, name='base'),
]