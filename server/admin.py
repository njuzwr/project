from django.contrib import admin
from server.models import Position, Status, User, DatabaseVersion, Order
# Register your models here.

admin.site.register(Position)
admin.site.register(Status)
admin.site.register(User)
admin.site.register(DatabaseVersion)
admin.site.register(Order)