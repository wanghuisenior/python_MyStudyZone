#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/17 11:07
"""
from django.urls import path

from study.views import bootstrap_views

# 在Ajax中的使用
# "{% url 'add_or_update_user' %}"
urlpatterns = [
    path('index', bootstrap_views.index, name='index'),
    path('icons', bootstrap_views.icons, name='icons'),
    path('bootstrap_grid', bootstrap_views.bootstrap_grid, name='bootstrap_grid'),
    path('bootstrap_table', bootstrap_views.bootstrap_table, name='bootstrap_table'),
    path('del_users', bootstrap_views.del_users, name='del_users'),
    path('create_or_update_user', bootstrap_views.create_or_update_user, name='create_or_update_user'),
    path('get_user_names', bootstrap_views.get_user_names, name='get_user_names'),
    path('bootstrap_validator', bootstrap_views.bootstrap_validator, name='bootstrap_validator'),
    path('bootstrap_navbar', bootstrap_views.bootstrap_navbar, name='bootstrap_navbar'),
]
