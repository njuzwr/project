# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json
from datetime import datetime, date, time
from random import randrange

from django.views.decorators.csrf import csrf_exempt
# test for post

from server.models import Position, DatabaseVersion, User, Order
# Create your views here.


def getversion(request):
    "用于获取位置信息的数据库版本，返回字符串"
    version = DatabaseVersion.objects.all().last().version
    response = "<html><body>%d </body></html>" % version
    return HttpResponse(response)
    # return HttpResponse(version)


def getposition(request):
    "用于处理客户端获取位置信息的请求"
    positions = Position.objects.all()
    position_num = str(Position.objects.all().count())
    position_json = serialize('json', positions)
    position_dict = json.loads(position_json)
    position = position_dict + [{"amounts": position_num}]
    return JsonResponse(position, safe=False)
    # return HttpResponse(position, content_type="text/plain")


def signup(request, username, password):
    "用于处理用户的注册及注册信息的保存"

    return HttpResponse('Succeed')


def signin(request, username, password):
    "用于处理用户的登录验证"

    return HttpResponse('Succeed')


@csrf_exempt
def getorderstatus(request):
    user = request.POST['username']
    u = get_object_or_404(User, username=user)
    s = get_object_or_404(Order, user=u).status
    r = '%d' % s
    return HttpResponse(r)


@csrf_exempt
def getchargingstatus(request):
    user = request.POST['username']
    u = get_object_or_404(User, username=user)
    c = get_object_or_404(Order, user=u).charge_p
    r = '%d' % c
    return HttpResponse(r)


@csrf_exempt
def getbalance(request):
    user = request.POST['username']
    bal = get_object_or_404(User, username=user).balance
    r = '<html><body>%s</body></html>' % str(bal)
    return HttpResponse(r)


@csrf_exempt
def orders1(request):
    # 获取post表单内容
    stime = request.POST['stime']
    etime = request.POST['etime']
    t = request.POST['type']
    # 利用集合set判断时间是否可用
    dt1 = datetime.combine(date.today(), time.min)
    dt2 = datetime.combine(date.today(), time(23, 59, 59))
    ds1 = int(datetime.timestamp(dt1))
    ds2 = int(datetime.timestamp(dt2))
    fullset = set(range(ds1, ds2 + 1, 600))  # 00:00:00~23:59:59

    st = int(float(stime))
    et = int(float(etime))
    time_need = set(range(st, et + 1, 600))

    pos = Position.objects.filter(type=t)
    pos_amount = len(pos)
    pos_available = []
    for i in range(pos_amount):
        time_available = fullset
        order = pos[i].order_set.filter(status=0)
        order_amount = len(order)
        for j in range(order_amount):
            s = int(datetime.timestamp(order[j].stime))
            e = int(datetime.timestamp(order[j].etime))
            time_used = set(range(s, e, 600))
            # 解决区间端点的问题
            time_available = time_available - time_used
        if time_need <= time_available:
            pos_available.append(pos[i].id)

    return JsonResponse(pos_available, safe=False)


@csrf_exempt
def orders2(request):
    # 获取表单内容
    user = request.POST['user']
    pid = request.POST['pid']
    stime = request.POST['stime']
    etime = request.POST['etime']
    t = request.POST['type']

    pos = get_object_or_404(Position, id=pid)
    # It is equivalent to:
    # try...except...

    u = get_object_or_404(User, username=user)

    st = datetime.fromtimestamp(stime)  # timestamp->datetime
    et = datetime.fromtimestamp(etime)

    c = ''
    for i in range(4):
        c += str(randrange(0, 10))  # This is augmented assignment
    o = Order.objects.create(position=pos, user=u, stime=st, etime=et, type=t, code=c)
    o.save()

    r = '<html><body>%s</body></html>' % c
    # return 4 bits random numbers

    return HttpResponse(c)


@csrf_exempt
def ordercancel(request):
    """
    用于订单的取消，取消成功则返回 succeed
    """
    user = request.POST['user']
    u = get_object_or_404(User, username=user)
    o = get_object_or_404(Order, user=u)
    o.status = 1
    o.save()
    return HttpResponse('Yes')


@csrf_exempt
# POST方式时必须加
def test(request):
    # data = json.loads(request.body)
    # username = data['username']
    # password = data['password']
    username = request.POST['username']
    password = request.POST['password']
    with open('D://d.txt', 'w+') as f:
        # f.write(str(username)+str(password))
        f.write(str(username) + str(password))
    return HttpResponse('Received')
