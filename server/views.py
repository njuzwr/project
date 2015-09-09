# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json
from datetime import datetime, date, time

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


def orders1(request, user, stime, etime, type):
    """
    订单的第一个请求阶段
    :param request:
    :param user: 用户名
    :param stime: 充电开始时间
    :param etime: 充电结束时间
    :param type: 车型
    :return:返回可用充电桩的pid
    """
    # 利用集合set判断时间是否可用
    dt1 = datetime.combine(date.today(), time.min)
    dt2 = datetime.combine(date.today(), time(23, 59, 59))
    ds1 = int(datetime.timestamp(dt1))
    ds2 = int(datetime.timestamp(dt2))
    fullset = set(range(ds1, ds2 + 1, 600))  # 00:00:00~23:59:59

    st = int(datetime.timestamp(stime))
    et = int(datetime.timestamp(etime))
    time_need = set(range(st, et + 1, 600))

    pos = Position.objects.all()
    pos_amount = Position.objects.count()
    pos_available = []
    for i in range(pos_amount):
        f1set = fullset
        order = pos[i].order_set.filter(status=0)
        order_amount = pos[i].order_set.filter(status=0).count()
        for j in range(order_amount):
            s = int(datetime.timestamp(order[j].stime))
            j = int(datetime.timestamp(order[j].etime))
            time_used = set(range(s, j + 1, 600))
            time_available = f1set - time_used
        if time_need <= time_available:
            pos_available.append(pos[i].id)

    return JsonResponse(pos_available)


def orders2(request, user, pid, stime, ctime, t):
    """
    订单请求的第二个阶段
    :param request:
    :param pid: 接收充电桩号pid
    :return:
    """
    # 试试使用timestamp类型，应该更加方便地计算时间
    pos = get_object_or_404(Position, id=pid)
    # It is equivalent to:
    # try...except...

    # Status.objects.filter(position = pos).update(status=2)
    u = get_object_or_404(User, username=user)

    st = datetime.fromtimestamp(stime)
    # timestamp->datetime
    o = Order.objects.create(position=pos, user=u, start_time=st, charge_time=ctime, type=t)
    o.save()
    return HttpResponse('Succeed!')


def cancel_order(request):
    """
    用于订单的取消，取消成功则返回 succeed
    """

    return HttpResponse('Succeed!')


@csrf_exempt
# POST方式时必须加
def test(request):
    json_data = request.read()
    # data = json.loads(json_data)
    with open('D://d.json', 'w+') as f:
        f.write(str(json_data))
    return HttpResponse('Received')
