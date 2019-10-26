from django.shortcuts import render
from django.db.models import Count, Sum, Max, Min
import re
from .models import Data2

# https://pypi.org/project/django-pivot/
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

def index(request):
    # list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('date1','member').annotate(headcnt=Count('id'))
    context = {'list1': []}
    return render(request, 'case002/index.html', context)
def s1(request):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('date1','member').annotate(headcnt=Count('id'))
    context = {'list1': list1}
    return render(request, 'case002/s1.html', context)

def s2(request):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('name').annotate(pointssum=Sum('points')).order_by('-pointssum')
    context = {'list1': list1}
    return render(request, 'case002/s2.html', context)

def s2_name(request,name):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(name=name).order_by('date1')
    context = {'list1': list1,'name': name}
    return render(request, 'case002/s2_name.html', context)
