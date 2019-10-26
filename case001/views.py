from django.shortcuts import render
from django.db.models import Count, Sum, Max, Min
import re
from .models import Data1

# https://pypi.org/project/django-pivot/
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

def index(request):
    list1 = Data1.objects.values('date1__year', 'date1__month').annotate(daycnt=Count(
        'date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))
    context = {'list1': list1}
    return render(request, 'case001/index.html', context)


def a8(request):

    list1 = Data1.objects.values('place', 'date1__year', 'date1__month').annotate(daycnt=Count('date1', distinct=True), headcnt=Count(
        'worker', distinct=True), idcnt=Count('id')).order_by('place', 'date1__year', 'date1__month')

    context = {'list': list1}
    return render(request, 'case001/a8.html', context)


def a1(request):

    list1 = Data1.objects.values('place').annotate(
        daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))

    context = {'list': list1}
    return render(request, 'case001/a1.html', context)

    def getLeadingNum(place):
        placeArr = re.findall('^(\d+)', x['place'])
        if placeArr:
            placeArr[0].zfill(5)

            # http://www.datasciencemadesimple.com/add-leading-preceding-zeros-python/
            # placeNum = num.apply(lambda x: '{0:0>10}'.format(x))
            # print('DEBUG...',num,placeNum)
            return placeArr[0].zfill(5)

        return place


def a1v2(request):

    list1 = Data1.objects.values('place').annotate(
        daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))

    def getLeadingNum(place):
        placeArr = re.findall('^(\d+)', x['place'])
        if placeArr:
            placeArr[0].zfill(5)
            return placeArr[0].zfill(5)
        return place

    for x in list1:

        placeArr = re.findall('^(\d+)', x['place'])
        x['placeNum'] = getLeadingNum(x['place'])

    list2 = list(list1)
    list2.sort(key=lambda x: x['placeNum'])

    context = {'list': list2}
    return render(request, 'case001/a1v2.html', context)


def getPlaceSorted(list1):
    def getLeadingNum(place):
        placeArr = re.findall('^(\d+)', x['place'])
        if placeArr:
            placeArr[0].zfill(5)
            return placeArr[0].zfill(5)
        return place

    for x in list1:

        placeArr = re.findall('^(\d+)', x['place'])
        x['placeNum'] = getLeadingNum(x['place'])

    list2 = list(list1)
    list2.sort(key=lambda x: x['placeNum'])
    return list2


def a2(request):

    list1 = Data1.objects.values('place').annotate(
        daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))

    # print("DEBUG ... ")
    for x in list1:
        list2 = Data1.objects.filter(place=x['place'], date1__year=2019, date1__month=7).values('place').annotate(
            daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))

        # 你會發現可能沒有，有的話也只有一筆
        # for x2 in list2:
        #     print('...',2019,7,x2)
        x['m1daycnt'] = x['m1headcnt'] = x['m1idcnt'] = 0
        if list2:
            x['m1daycnt'] = list2[0]['daycnt']
            x['m1headcnt'] = list2[0]['headcnt']
            x['m1idcnt'] = list2[0]['idcnt']

        # print(x)

    context = {'list': list1}
    return render(request, 'case001/a2.html', context)


def a2v2(request):

    list1 = Data1.objects.values('place').annotate(
        daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))

    for x in list1:
        list2 = Data1.objects.filter(place=x['place'], date1__year=2019, date1__month=7).values('place').annotate(
            daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))

        # 你會發現可能沒有，有的話也只有一筆
        # for x2 in list2:
        #     print('...',2019,7,x2)
        x['m1daycnt'] = x['m1headcnt'] = x['m1idcnt'] = 0
        if list2:
            x['m1daycnt'] = list2[0]['daycnt']
            x['m1headcnt'] = list2[0]['headcnt']
            x['m1idcnt'] = list2[0]['idcnt']

        # print(x)

    context = {'list': getPlaceSorted(list1)}
    return render(request, 'case001/a2v2.html', context)


def a3(request):

    list1 = Data1.objects.values('place').annotate(
        daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))

    def getMoList(yr, mo):
        list2 = Data1.objects.filter(place=x['place'], date1__year=yr, date1__month=mo).values('place').annotate(
            daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))
        return list2
    for x in list1:
        # list2 = Data1.objects.filter(place=x['place'], date1__year=2019, date1__month=7).values('place').annotate(
        #     daycnt=Count('date1',distinct=True),headcnt=Count('worker',distinct=True),idcnt=Count('id'))

        m1 = getMoList(2019, 7)
        m2 = getMoList(2019, 8)
        m3 = getMoList(2019, 9)

        x['m1daycnt'] = x['m1headcnt'] = x['m1idcnt'] = ''
        x['m2daycnt'] = x['m2headcnt'] = x['m2idcnt'] = ''
        x['m3daycnt'] = x['m3headcnt'] = x['m3idcnt'] = ''
        if m1:
            x['m1daycnt'] = m1[0]['daycnt']
            x['m1headcnt'] = m1[0]['headcnt']
            x['m1idcnt'] = m1[0]['idcnt']
        if m2:
            x['m2daycnt'] = m2[0]['daycnt']
            x['m2headcnt'] = m2[0]['headcnt']
            x['m2idcnt'] = m2[0]['idcnt']
        if m3:
            x['m3daycnt'] = m3[0]['daycnt']
            x['m3headcnt'] = m3[0]['headcnt']
            x['m3idcnt'] = m3[0]['idcnt']

        # print(x)

    context = {'list': list1}
    return render(request, 'case001/a3.html', context)


def getList1():
    list1 = Data1.objects.values('place').annotate(
        daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))

    def getMoList(yr, mo):
        list2 = Data1.objects.filter(place=x['place'], date1__year=yr, date1__month=mo).values('place').annotate(
            daycnt=Count('date1', distinct=True), headcnt=Count('worker', distinct=True), idcnt=Count('id'))
        return list2
    for x in list1:
       
        m1 = getMoList(2019, 7)
        m2 = getMoList(2019, 8)
        m3 = getMoList(2019, 9)

        x['m1daycnt'] = x['m1headcnt'] = x['m1idcnt'] = ''
        x['m2daycnt'] = x['m2headcnt'] = x['m2idcnt'] = ''
        x['m3daycnt'] = x['m3headcnt'] = x['m3idcnt'] = ''
        if m1:
            x['m1daycnt'] = m1[0]['daycnt']
            x['m1headcnt'] = m1[0]['headcnt']
            x['m1idcnt'] = m1[0]['idcnt']
        if m2:
            x['m2daycnt'] = m2[0]['daycnt']
            x['m2headcnt'] = m2[0]['headcnt']
            x['m2idcnt'] = m2[0]['idcnt']
        if m3:
            x['m3daycnt'] = m3[0]['daycnt']
            x['m3headcnt'] = m3[0]['headcnt']
            x['m3idcnt'] = m3[0]['idcnt']
    return list1


def a3v2(request):

    list1 = getList1()
    context = {'list': getPlaceSorted(list1)}
    return render(request, 'case001/a3v2.html', context)

def a4v2(request):

    list1 = getList1()
    context = {'list': getPlaceSorted(list1)}
    return render(request, 'case001/a4v2.html', context)

def b1(request,yr,mo):
    key={'yr':yr,'mo':mo,}
    # list1 =  Data1.objects.filter(date1__year=yr, date1__month=mo).values('place','date1__day').annotate(idcnt=Count('id'))
    pivot1 =pivot(Data1.objects.filter(date1__year=yr, date1__month=mo),'place','date1__day','id',aggregation=Count)
    # for x in pivot1:
    #     print (x)
    context = {'key':key,'list': getPlaceSorted(pivot1)}
    return render(request, 'case001/b1.html', context)

def b1_list(request):

    list1 =  Data1.objects.values('date1__year','date1__month').annotate(idcnt=Count('id'),placecnt=Count('place',distinct=True)).order_by('date1__year','date1__month')
    context = {'list': list1}
    return render(request, 'case001/b1_list.html', context)
