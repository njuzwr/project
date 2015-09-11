# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from datetime import datetime, date, time
from random import randrange

from django.views.decorators.csrf import csrf_exempt
# test for post

from server.models import Position, DatabaseVersion, User, Order
# Create your views here.


def getversion(request):
    """用于获取位置信息的数据库版本，返回字符串"""
    version = DatabaseVersion.objects.all().last().version
    r = "%d" % version
    return HttpResponse(r)
    # return HttpResponse(version)


def getdatabase(request):
    """用于处理客户端获取位置信息的请求"""
    positions = Position.objects.all()
    # position_num = str(Position.objects.all().count())
    position_json = serialize('json', positions)
    # position_dict = json.loads(position_json)
    # position = position_dict + [{"amounts": position_num}]
    # return JsonResponse(position_dict, safe=False)
    return HttpResponse(position_json, content_type="application/json")


@csrf_exempt  # POST方法必须加上
def signup(request, username, password):
    """用于处理用户的注册及注册信息的保存"""

    return HttpResponse('Succeed')


@csrf_exempt
def login(request):
    """用于处理用户的登录验证"""
    un = request.POST['username']
    pw = request.POST['password']
    p = get_object_or_404(User, username=un).password
    if pw == p:
        r = 'true'
    else:
        r = 'false'
    return HttpResponse('%s' % r)


@csrf_exempt
def getorderstatus(request):
    user = request.POST['username']
    u = get_object_or_404(User, username=user)
    o = Order.objects.filter(user=u).last()
    s = o.status
    # 每个用户只能用一个未完成的订单状态
    # 如果正在充电，则返回充电百分比
    r = 'None'
    if s == 0:  # 充电未完成
        r = {'stime': int(datetime.timestamp(o.stime)), 'etime': int(datetime.timestamp(o.etime)),
             'pid': o.position_id, 'status': o.status, 'code': o.code}
    elif s == 2:  # 充电过程中，返回充电百分比
        r = {'stime': int(datetime.timestamp(o.stime)), 'etime': int(datetime.timestamp(o.etime)),
             'pid': o.position_id, 'status': o.charge_p, 'code': o.code}
    else:  # 订单已完成
        r = {'stime': 0, 'etime': 0, 'pid': 0, 'status': o.status, 'code': 'xxxx'}
    return JsonResponse(r)


@csrf_exempt
def getchargingstatus(request):
    user = request.POST['username']
    u = get_object_or_404(User, username=user)
    o = Order.objects.filter(user=u).last()
    s = o.charge_p
    return HttpResponse('%s' % str(s))


@csrf_exempt
def getbalance(request):
    user = request.POST['username']
    bal = get_object_or_404(User, username=user).balance
    r = '%s' % str(bal)
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
    user = request.POST['username']
    pid = request.POST['pid']
    stime = request.POST['stime']
    etime = request.POST['etime']
    t = request.POST['type']

    pos = get_object_or_404(Position, id=pid)
    # It is equivalent to:
    # try...except...

    u = get_object_or_404(User, username=user)
    orderstatus = Order.objects.filter(user=u).filter(status=0)

    st = datetime.fromtimestamp(int(float(stime)))  # timestamp->datetime
    et = datetime.fromtimestamp(int(float(etime)))

    c = ''
    for i in range(4):
        c += str(randrange(0, 10))  # This is augmented assignment

    if orderstatus:  # 判断是否有未完成的订单
        r = 'Unfinished order'
    else:
        o = Order.objects.create(position=pos, user=u, stime=st, etime=et, type=t, code=c)
        o.save()
        r = 'success, %s' % c  # return 4 bits random numbers
    return HttpResponse(r)


@csrf_exempt
def ordercancel(request):
    """
    用于订单的取消，取消成功则返回 succeed
    """
    user = request.POST['username']
    u = get_object_or_404(User, username=user)
    o = Order.objects.filter(user=u).last()  # 最近的订单
    o.status = 1
    o.save()
    return HttpResponse('yes')


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


def test2(request, i):
    x = get_object_or_404(Position, id=i).id
    return HttpResponse('%d' % x)
