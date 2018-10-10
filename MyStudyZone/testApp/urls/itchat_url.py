#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/10/9 17:35
"""
from sys import path

from testApp.views import itchat_views

urlpatterns = [
    path('index', itchat_views.index, name='index'),
]
