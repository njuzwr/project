"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from server.views import getversion, getposition, order, test
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getversion/', getversion),
    url(r'^getposition/', getposition),
    url(r'^order/(?P<pid>\d+)/(?P<stime>\d+.\d+)/(?P<ctime>\d+)/(?P<name>\w+)/(?P<s>\d+)/', order),
    # url(r'^order/\d+/\d{4}-\d+-\d+%\d+/',test),
    # url(r'^test/(?P<pid>\d+)/(?P<s>\d+)/',test),
    url(r'^test/', test)
    # 匹配 2015-9-12 8：00
    # 采用timestamp类型


]