from django.urls import path, include
from .views import *  
urlpatterns=[
path('',Index.as_view(), name='index'),
path('populate21/', view=PopulateFromCSV, name = 'populate'),
path('sections',Sections.as_view(), name='sections'),
path('department/<int:id>',Departments.as_view(), name='departments'),
    ]