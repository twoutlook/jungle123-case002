from django.shortcuts import render
from django.db.models import Count, Sum, Max, Min
import re
from .models import Data2
from .models import Best


# https://pypi.org/project/django-pivot/
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

def index(request):
    # list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('date1','member').annotate(headcnt=Count('id'))
    context = {'list1': []}
    return render(request, 'case002/index.html', context)
def s1(request):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('date1','member').annotate(headcnt=Count('id'))
    
    pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    for x in pivot_table:
        x['total']=x['Member']+x['Guest']
        # print(x)
    context = {'list1': pivot_table}
    return render(request, 'case002/s1.html', context)

def s1_date(request,date1):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(date1=date1).values('date1','member').annotate(headcnt=Count('id'))
    list2 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(date1=date1).order_by('-member','name')
    
    pivot_table = pivot(list1, 'date1', 'member', 'id',aggregation=Count)
    for x in pivot_table:
        try:
    #your code
            x['total']=x['Member']+x['Guest']
        
        except Exception as ex:
            # print(ex)
            x['total']=x['Member']
        # print(x)
   
            
        # print(x)
    context = {'list1': pivot_table,'list2':list2}
    return render(request, 'case002/s1_date.html', context)

def s2(request):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').values('name').annotate(pointssum=Sum('points')).filter(pointssum__gt = 0).order_by('-pointssum')
    context = {'list1': list1}
    return render(request, 'case002/s2.html', context)

def s2_name(request,name):
    list1 = Data2.objects.exclude(role='---').exclude(role='Absence').filter(name=name).order_by('date1')
    context = {'list1': list1,'name': name}
    return render(request, 'case002/s2_name.html', context)

def s3(request):
    list1 = Data2.objects.filter(role__in = ['Ah-counter','GE','Grammarian','TME','TT Evaluator','TT-master','Timer'])
    pivot_table = pivot(list1, 'date1', 'role', 'name',aggregation=Min)
    for x in pivot_table:
        x['Ah']=x['Ah-counter']
        x['TT_Evaluator']=x['TT Evaluator']
        x['TT_master']=x['TT-master']
        # print(x)
    context = {'list1': pivot_table}
    return render(request, 'case002/s3.html', context)

def best(request):
    pivot_table = pivot(Best, 'date1', 'title', 'name',aggregation=Min)
    # for x in pivot_table:
        # print(x)
    context = {'list1': pivot_table}
    return render(request, 'case002/best.html', context)


def s4(request):
    list1 = Data2.objects.filter(role__in = ['Speaker','IE']).values('date1').annotate(cnt=Count('id')).order_by('date1')
    # list1 = Data2.objects.filter(role__in = ['Speaker','IE']).order_by('date1','-role','name')
    for x in list1:
        list2 = Data2.objects.filter(date1= x['date1'],role = 'Speaker')
        list3 = Data2.objects.filter(date1= x['date1'],role = 'IE')
        speaker = ''
        ie = ''

        def getNameStr(listx):
            speaker = ''
            cnt = 0
            for x2 in listx:
                cnt += 1
                speaker = speaker +"("+str(cnt)+")"+ x2.name+" "
            return speaker

        # cnt = 0
        # for x2 in list2:
        #     cnt += 1
        #     speaker = speaker +"("+str(cnt)+")"+ x2.name+" "

        x['speaker']=getNameStr(list2)
        x['ie']=getNameStr(list3)

        # cnt = 0
        # for x3 in list3:
        #     cnt += 1
        #     ie = ie +"("+str(cnt)+")"+ x3.name+" "

        # x['ie']=ie
    
    
        # print(x)
    context = {'list1': list1}
    return render(request, 'case002/s4.html', context)
