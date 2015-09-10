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

from server.views import getversion, getposition, orders1, orders2, test
from server.views import getorderstatus, getchargingstatus, getbalance, ordercancel
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getversion/', getversion, name='getversion'),
    url(r'^getposition/', getposition),
    url(r'^getorderstatus/', getorderstatus),
    url(r'^getchargingstatus/', getchargingstatus),
    url(r'^getbalance/', getbalance),
    url(r'^orders1/', orders1),
    url(r'^orders2/', orders2),
    url(r'^ordercancel', ordercancel),
    url(r'^test/', test),



]