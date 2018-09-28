#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/25 10:14
"""
from django.conf.urls import url
from django.urls import path, re_path
from study.views import user_views

urlpatterns = [
    path('user_manage', user_views.user_manage, name='user_manage'),
    path('search', user_views.search, name='search'),
    path('get/<uuid:user_id>', user_views.get_user_by_id, name='get'),
    #将id放在url路径当中传递
    path('delete_user_by_id/<uuid:user_id>', user_views.delete_user_by_id, name='delete'),
    #将id作为请求参数传递
    path('delete_user_by_id1', user_views.delete_user_by_id1),

]
