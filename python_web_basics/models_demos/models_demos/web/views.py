from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from models_demos.web.models import Employee, Department, Project


# Create your views here.
def index(request):
    employees = [e for e in Employee.objects.all() if e.department_id == 1]
    # employees2 = Employee.objects.filter(department_id=2) \
    # In filter department__name == deparment.name
    employees2 = Employee.objects.filter(department__name='Engineering') \
        .order_by('last_name', 'first_name')
    # employee_list = list(employee)
    # print(list(User.objects.all()))
    # print(list(Department.objects.all()))
    # print(employee_list)
    # print(employee)

    # Get return an object! not querySet
    # Get returns single object nad throws when none or multiple results
    # Get is eager and does not reutn a QuerySet

    # get_object_or_404(Employee, level=Employee.LEVEL_REGULAR)

    Employee.objects.filter(level=Employee.LEVEL_SENIOR) \
        .first()

    department = Department.objects.get(pk=1)
    # print(Employee.objects.get(level=Employee.LEVEL_JUNIOR))
    print(department)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department
    }

    return render(request, 'index.html', context=context)


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }

    return render(request, 'department-details.html', context=context)

def delete_employee(request, pk):
    department_pk = 1

    # When restricted this must be done explicitly
    # This Casdade this is done implicitly
    Employee.objects.filter(department_id=department_pk) \
        .delete()

    get_object_or_404(Department, pk=department_pk) \
        .delete()
    # employee = get_object_or_404(Employee, pk=pk)
    # employee.delete()
    #
    # # Delete all projects with this criteria
    # Project.objects.filter() \
    #     .delete()
    # #Deletes all projects
    # Project.objects.all() \
    #     .delete()
    return redirect('index')