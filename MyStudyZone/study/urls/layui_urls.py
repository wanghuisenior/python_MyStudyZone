#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/17 11:07
"""
from django.conf.urls import url
from django.urls import path

from study.views import layui_views

# 在Ajax中的使用
# "{% url 'add_or_update_user' %}"
urlpatterns = [
    path('layui_href', layui_views.layui_href, name='layui_href'),
    path('layui_grid', layui_views.layui_grid, name='layui_grid'),
    path('layui_admin1', layui_views.layui_admin1, name='layui_admin1'),
    path('layui_button', layui_views.layui_button, name='layui_button'),
    path('layui_carousel', layui_views.layui_carousel, name='layui_carousel'),
    path('layui_code', layui_views.layui_code, name='layui_code'),
    path('layui_element', layui_views.layui_element, name='layui_element'),
    path('layui_form', layui_views.layui_form, name='layui_form'),
    path('layui_laydate', layui_views.layui_laydate, name='layui_laydate'),
    path('layui_layedit', layui_views.layui_layedit, name='layui_layedit'),
    path('layui_layer', layui_views.layui_layer, name='layui_layer'),
    path('layui_laypage', layui_views.layui_laypage, name='layui_laypage'),
    path('layui_rate', layui_views.layui_rate, name='layui_rate'),
    path('layui_responsive', layui_views.layui_responsive, name='layui_responsive'),
    path('layui_table', layui_views.layui_table, name='layui_table'),
    path('layui_tree', layui_views.layui_tree, name='layui_tree'),
    path('layui_upload', layui_views.layui_upload, name='layui_upload'),
    path('layui_util', layui_views.layui_util, name='layui_util'),
    path('layui_mytest', layui_views.layui_mytest, name='layui_mytest'),
    # admin 框架
    path('layui_admin_login', layui_views.layui_admin_login, name='layui_admin_login'),
    path('layui_admin_index', layui_views.layui_admin_index, name='layui_admin_index'),
    path('layui_main', layui_views.layui_main, name='layui_main'),
    path('layui_admin_grid', layui_views.layui_admin_grid, name='layui_admin_grid'),
    path('layui_admin_table', layui_views.layui_admin_table, name='layui_admin_table'),
    path('layui_admin_layer', layui_views.layui_admin_layer, name='layui_admin_layer'),
]
