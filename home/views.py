from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import *
import csv
from .constants import *


def PopulateFromCSV(request):


    dataReader = csv.reader(open('stafflist.csv'), delimiter=',', quotechar='"')

    des = []
    for row in dataReader:
        if row[2]:
            des.append(row[2].strip())

    des = list(set(des))
    designs = []
    i=1
    for d in des:
        de = Designation()
        de.designation_number = i
        de.designation_name = d
        de.save()
        i = i+1

    return HttpResponse("ok")

'''
def PopulateFromCSV(request):


    dataReader = csv.reader(open('stafflist.csv'), delimiter=',', quotechar='"')

    for row in dataReader:
        if row[0]: employee_id = row[0]
        else: continue
        if row[1]: name = row[1]
        else: continue
        if row[2]: 
            designation = row[2]
            designation=designation.strip()
            designation = Designation.objects.filter(designation_name=designation)[0]
        else: designation = Designation.objects.get(designation_number=0)

        if row[3]: 
            department = row[3]
            department = department.strip()
            department = Department.objects.filter(department_name=department)[0]
        else: department = Department.objects.get(department_number=0)
        

        emp = Employee()
        emp.employee_id = employee_id
        emp.name = name
        emp.personal_phone_no = "9876543210"
        emp.other_phone_no = "7894561320"
        emp.email_id = ""
        emp.department_no = department
        emp.designation_no = designation
        emp.quarter_number = "125"
        emp.residence_number = "59"
        emp.office_number = "2045"
        emp.save()
    return HttpResponse("ok")
'''

class Index(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['home_active'] = "active"
        context['departments'] = Department.objects.filter(department_type_id=C_department_type).order_by('department_name')
        context['sections'] = Department.objects.filter(department_type_id=C_section_type).order_by('department_name')
        context['incharges'] = Department.objects.filter(department_type_id=C_incharge_type).order_by('department_name')
        context['centers'] = Department.objects.filter(department_type_id=C_center_type).order_by('department_name')
        return context


class Employees(TemplateView):
    template_name = 'home/employees.html'

    def get_context_data(self, **kwargs):
        context = super(Employees, self).get_context_data(**kwargs)
        context['employees_active'] = "active"
        context['departments'] = Department.objects.filter(department_type_id=C_department_type).order_by('department_name')
        context['sections'] = Department.objects.filter(department_type_id=C_section_type).order_by('department_name')
        context['incharges'] = Department.objects.filter(department_type_id=C_incharge_type).order_by('department_name')
        context['centers'] = Department.objects.filter(department_type_id=C_center_type).order_by('department_name')
        context['employees'] = Employee.objects.all().order_by('name')
        return context



class Departments(TemplateView):
    template_name = 'home/department.html'

    def get_context_data(self, **kwargs):
        context = super(Departments, self).get_context_data(**kwargs)
        context['department_active'] = "active"
        context['deptId'] = kwargs['id']
        context['department'] = Department.objects.get(department_number=context['deptId'])
        context['departments'] = Department.objects.filter(department_type_id=C_department_type).order_by('department_name')
        context['sections'] = Department.objects.filter(department_type_id=C_section_type).order_by('department_name')
        context['incharges'] = Department.objects.filter(department_type_id=C_incharge_type).order_by('department_name')
        context['centers'] = Department.objects.filter(department_type_id=C_center_type).order_by('department_name')
        context['employees'] = Employee.objects.filter(department_no=context['department']).order_by('name')
        return context

