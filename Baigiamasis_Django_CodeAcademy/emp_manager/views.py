from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Role
from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages


def base_view(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')


def all_employees(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_employee(request):
    roles = Role.objects.all()
    context = {'roles': roles}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        role_id = request.POST['role']
        email = request.POST['email']
        role = Role.objects.get(id=role_id)
        
        # Validate phone number
        if not phone.isdigit() or not phone.startswith('86'):
            messages.error(request, 'Netinkamas numeris!')
            return render(request, 'add_emp.html', context)
        
        new_emp = Employee(first_name=first_name, last_name=last_name, phone=int(phone), role=role, hire_date=datetime.now(), email=email)
        new_emp.save()
        messages.success(request, "Darbuotojas pridėtas sėkmingai!")
        return render(request, 'add_emp.html', context)
    elif request.method=='GET':
        return render(request, 'add_emp.html', {'roles': roles})
    else:
        messages.error(request, "Nutiko kažkas baisaus! Darbuotojas nepridėtas :(")
        return render(request, 'add_emp.html', context)


def remove_employee(request):
    if request.method == 'POST':
        emp_id = request.POST.get('employee_id')
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request, "Darbuotojas ištrintas sėkmingai!")
        except:
            messages.error(request, "Įvyko klaida, bandykite dar kartą.")

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)




def filter_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {
            'emps': emps,
            'name': name,
            'role': role
        }
        return render(request, 'view_all_emp.html', context)
    else:
        roles = Role.objects.all()
        context = {
            'roles': roles
        }
        return render(request, 'filter_emp.html', context)

    
def update_employee(request, emp_id=0):
    emp_to_be_updated = get_object_or_404(Employee, id=emp_id)
    roles = Role.objects.all()
    if request.method == 'POST':
        emp_to_be_updated.first_name = request.POST['first_name']
        emp_to_be_updated.last_name = request.POST['last_name']
        emp_to_be_updated.phone = request.POST['phone']
        emp_to_be_updated.role = Role.objects.get(id=request.POST['role'])
        emp_to_be_updated.email = request.POST['email']
        emp_to_be_updated.save()
        messages.success(request,'Darbuotojo informacija atnaujinta sėkmingai!')
        return redirect('all_emp')
    else:
        context = {
            'emp': emp_to_be_updated,
            'emp_id': emp_id,
            'roles': roles,
        }
        return render(request, 'update_emp.html', context)




