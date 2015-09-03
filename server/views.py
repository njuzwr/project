# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json
from urllib.parse import unquote
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


def order(request, pid, s_time, c_time, name, size):
    """用于处理订单的预订，返回预约成功的标志位
    order_id:所预约的充电桩编号id
    order_time:要预约的时间
    charge_time:充电时间
    username:用户名
    """
    # 试试使用timestamp类型，应该更加方便地计算时间
    p = Position.objects.get(id=pid)
    Status.objects.filter(position = p).update(status=2)
    u = User.objects.get(username = name)
    o = Order.objects.create(position = p, user= u, start_time=unquote(s_time), charge_time = c_time, size = 1)
    o.save()
    return HttpResponse('Succeed!')
