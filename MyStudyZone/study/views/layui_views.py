#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/20 8:15
"""
from django.shortcuts import render


def layui_home(request):
    return render(request, 'layui_home.html')


def layui_grid(request):
    return render(request, 'layui_grid.html')


def layui_button(request):
    return render(request, 'layui_button.html')


def layui_carousel(request):
    # 轮播组件
    return render(request, 'layui_carousel.html')


def layui_admin(request):
    return render(request, 'layui_admin.html')


def layui_code(request):
    # 代码修饰器
    return render(request, 'layui_code.html')


def layui_element(request):
    # 常用元素
    return render(request, 'layui_element.html')


def layui_form(request):
    # 表单
    return render(request, 'layui_form.html')


def layui_laydate(request):
    # 时间选择器
    return render(request, 'layui_laydate.html')


def layui_layedit(request):
    # 富文本编辑器
    return render(request, 'layui_layedit.html')


def layui_layer(request):
    # 弹出层
    return render(request, 'layui_layer.html')


def layui_laypage(request):
    # 分页
    return render(request, 'layui_laypage.html')


def layui_rate(request):
    # 评分
    return render(request, 'layui_rate.html')


def layui_responsive(request):
    # 评分
    return render(request, 'layui_responsive.html')


def layui_table(request):
    # 表格
    return render(request, 'layui_table.html')


def layui_tree(request):
    # 表格
    return render(request, 'layui_tree.html')


def layui_upload(request):
    # 表格
    return render(request, 'layui_upload.html')


def layui_util(request):
    # 表格
    return render(request, 'layui_util.html')
