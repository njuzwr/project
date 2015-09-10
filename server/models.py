# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class DatabaseVersion(models.Model):
    version = models.IntegerField()
    log = models.CharField(max_length=100, default=None)
    author = models.CharField(max_length=20, default=None)
    time_revise = models.DateTimeField(default=None)

    def __str__(self):
        return str(self.version)


class Position(models.Model):
    type = models.CharField(max_length=10, default=None)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username


class Order(models.Model):
    position = models.ForeignKey(Position)
    user = models.OneToOneField(User, primary_key=True)
    stime = models.DateTimeField(default=None)  # 充电开始时间
    etime = models.DateTimeField(default=None)  # 充电结束时间
    type = models.CharField(max_length=5, default=None)  # 车型
    status = models.IntegerField(default=0)  # 订单状态：订单完成或取消为1，默认为0,处于充电中为2
    charge_p = models.IntegerField(default=0)  # 充电百分比 1-100的整数
    code = models.CharField(max_length=4, default=None)

    def __str__(self):
        return self.user.username
# Fields:position(many-to-one relationship), user(one-to-one relationship)


