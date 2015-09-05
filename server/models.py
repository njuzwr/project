# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class Position(models.Model):
    size_supported = models.CharField(max_length=5)
    longitude = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)
# Fields:id, size, longitude, latitude


class Status(models.Model):
    position = models.OneToOneField(Position,primary_key=True)
    status = models.IntegerField()

    def __str__(self):
        return str(self.position_id)
# Fields: position(One-to-One relationship), status
# status:0-avaliable -1-charging -2-not avaliable, cannot be ordered
#       :>1-amounts of orders


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=15, decimal_places=5)

    def __str__(self):
        return self.username


class Order(models.Model):
    position = models.ForeignKey(Position)
    user = models.OneToOneField(User, primary_key=True)
    start_time = models.DateTimeField()
    charge_time = models.CharField(max_length=5,default=None)
    size = models.CharField(max_length=5)


    def __str__(self):
        return self.user.username
# Fields:position(many-to-one relationship), user(one-to-one relationship)


class DatabaseVersion(models.Model):
    version = models.IntegerField()
    log = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    time_revise = models.DateTimeField()

    def __str__(self):
        return str(self.version)
