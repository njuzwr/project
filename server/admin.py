# -*- coding:utf-8 -*-
from django.contrib import admin
from server.models import Position, User, DatabaseVersion
# Register your models here.

# customize admin site


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'longitude', 'latitude', 'type')
    search_fields = ['id']


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('position', 'user', 'stime', 'etime', 'type')
#     search_fields = ['position']


admin.site.register(Position, PositionAdmin)
admin.site.register(User)
admin.site.register(DatabaseVersion)
# admin.site.register(Order, OrderAdmin)
