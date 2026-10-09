
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Employee


def home(request):
    return render(request, 'home.html')


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {
        'employees': employees,
    })


@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {
        'employee': employee,
    })