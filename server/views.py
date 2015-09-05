# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
# test for post

from server.models import Position, DatabaseVersion, User, Status, Order
# Create your views here.


def getversion(request):
    "用于获取位置信息的数据库版本，返回json数据格式"
    version = DatabaseVersion.objects.all().last().version
    response = "<html><body>Database version is %d </body></html>" % version
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


def order(request, pid, stime, ctime, name, s):
    """用于处理订单的预订，返回预约成功的标志位
    pid:所预约的充电桩编号id
    stime:要预约的时间
    ctime:充电时间
    name:用户名
    s:车型
    """
    # 试试使用timestamp类型，应该更加方便地计算时间
    pos = get_object_or_404(Position, id=pid)
    # It is equivalent to:
    # try...except...

    # Status.objects.filter(position = pos).update(status=2)
    get_list_or_404(Status, position=pos).update(status=2)
    u = get_object_or_404(User, username=name)

    st = datetime.fromtimestamp(stime)
    # timestamp->datetime
    o = Order.objects.create(position=pos, user=u, start_time=st, charge_time=ctime, size=s)
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
