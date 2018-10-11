#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/10/9 17:35
"""
from django.urls import path

from testApp.views import itchat_views

urlpatterns = [
    path('index', itchat_views.index, name='itchat_index'),
    path('wechat_login', itchat_views.wechat_login, name='wechat_login'),
]
