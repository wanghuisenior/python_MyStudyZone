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
    path('del_users', user_views.del_users, name='del_users'),
    path('create_or_update_user', user_views.create_or_update_user, name='create_or_update_user'),
    path('get_user_names', user_views.get_user_names, name='get_user_names'),
    path('update_user_info', user_views.update_user_info, name='update_user_info'),
    path('test_user_available', user_views.test_user_available, name='test_user_available'),
    path('create_user', user_views.create_user, name='create_user'),
]
