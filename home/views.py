from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import *
import csv

'''
def PopulateFromCSV(request):

    Department.objects.all().delete()
    Designation.objects.all().delete()
    return HttpResponse("ok")

    dataReader = csv.reader(open('teldir.csv'), delimiter=',', quotechar='"')

    des = []
    for row in dataReader:
        if row[2]:
            des.append(row[2].strip())

    des = list(set(des))
    designs = []
    i=1
    for d in des:
        de = Department()
        de.department_number = i
        de.department_name = d
        de.department_short_name = d
        de.save()
        i = i+1

    return HttpResponse("ok")



def PopulateFromCSV(request):


    dataReader = csv.reader(open('teldir.csv'), delimiter=',', quotechar='"')

    id = 1
    for row in dataReader:
        if row[0]: name = row[0]
        else: continue
        if row[1]: 
            designation = row[1]
            designation=designation.strip()
            designation = Designation.objects.filter(designation_name=designation)[0]
        else: designation = Designation.objects.get(designation_number=0)

        if row[2]: 
            department = row[2]
            department = department.strip()
            department = Department.objects.filter(department_name=department)[0]
        else: department = Department.objects.get(department_number=0)
        
        if row[3]: officeno = row[3]
        else: officeno = "0"
        if row[4]: resno = row[4]
        else: resno = "0"
        if row[5]: qtsno = row[5]
        else: qtsno = "0"
        if row[6]: mobile1 = row[6]
        else: mobile1 = "0"
        
        if row[7] is not None: mobile2 = row[7]
        else: mobile2 = "0"

        emp = Employee()
        emp.employee_id = id
        emp.name = name
        emp.personal_phone_no = mobile1
        emp.other_phone_no = mobile2
        emp.email_id = ""
        emp.department_no = department
        emp.designation_no = designation
        emp.quarter_number = qtsno
        emp.residence_number = resno
        emp.office_number = officeno
        #emp.save()
        id = id+1
    return HttpResponse("ok")
'''



class Index(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['home_active'] = "active"
        context['departments'] = Department.objects.all().order_by('department_name')
        context['designations'] = Designation.objects.all().order_by('designation_name')
        context['employees'] = Employee.objects.all().order_by('name')
        return context



class Departments(TemplateView):
    template_name = 'home/department.html'

    def get_context_data(self, **kwargs):
        context = super(Departments, self).get_context_data(**kwargs)
        context['department_active'] = "active"
        context['deptId'] = kwargs['id']
        context['department'] = Department.objects.get(department_number=context['deptId'])
        context['departments'] = Department.objects.all().order_by('department_name')
        context['designations'] = Designation.objects.all().order_by('designation_name')
        context['employees'] = Employee.objects.filter(department_no=context['department']).order_by('name')
        return context

class Designations(TemplateView):
    template_name = 'home/designation.html'

    def get_context_data(self, **kwargs):
        context = super(Designations, self).get_context_data(**kwargs)
        context['designation_active'] = "active"
        context['desId'] = kwargs['id']
        context['designation'] = Designation.objects.get(designation_number=context['desId'])
        context['departments'] = Department.objects.all().order_by('department_name')
        context['designations'] = Designation.objects.all().order_by('designation_name')
        context['employees'] = Employee.objects.filter(designation_no=context['designation']).order_by('name')
        return context

