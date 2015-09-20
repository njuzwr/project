# -*- coding:utf-8 -*-
from django.contrib import admin
from server.models import Position, User, DatabaseVersion, Order
# Register your models here.

# customize admin site


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'longitude', 'latitude', 'type')
    search_fields = ['id']


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'balance')
    search_fields = ['username']


class DatabaseVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'log', 'author', 'time_revise')
    search_fields = ['id']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'stime', 'etime', 'type', 'status', 'charge_p', 'code', 'position', 'user')
    search_fields = ['position']


admin.site.register(Position, PositionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(DatabaseVersion, DatabaseVersionAdmin)
admin.site.register(Order, OrderAdmin)
