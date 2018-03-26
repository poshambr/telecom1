from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import *
import csv


def PopulateFromCSV(request):


    dataReader = csv.reader(open('teldir.csv'), delimiter=',', quotechar='"')

    des = []
    for row in dataReader:
        if row[3] != 'Dept_Name':
            des.append(row[2])

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




class Index(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['home_active'] = "active"
        context['departments'] = Department.objects.all().order_by('department_number')
        return context


class Sections(TemplateView):
    template_name = 'home/sections.html'

    def get_context_data(self, **kwargs):
        context = super(Sections, self).get_context_data(**kwargs)
        context['sections_active'] = "active"
        context['departments'] = Department.objects.all().order_by('department_number')
        return context


class Departments(TemplateView):
    template_name = 'home/department.html'

    def get_context_data(self, **kwargs):
        context = super(Departments, self).get_context_data(**kwargs)
        context['department_active'] = "active"
        context['deptId'] = kwargs['id']
        context['deptName'] = Department.objects.filter(department_number=context['deptId'])[0]
        context['departments'] = Department.objects.all().order_by('department_number')
        return context
