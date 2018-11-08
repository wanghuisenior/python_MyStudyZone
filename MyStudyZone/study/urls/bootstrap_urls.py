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
    path('bootstrap_index', bootstrap_views.bootstrap_index, name='bootstrap_index'),
    path('confirm_with_bs', bootstrap_views.confirm_with_bs, name='confirm_with_bs'),
    path('bootstrap_grid', bootstrap_views.bootstrap_grid, name='bootstrap_grid'),
    path('bootstrap_table', bootstrap_views.bootstrap_table, name='bootstrap_table'),

    path('bootstrap_validator', bootstrap_views.bootstrap_validator, name='bootstrap_validator'),
    path('bootstrap_table_edit', bootstrap_views.bootstrap_table_edit, name='bootstrap_table_edit'),
]
