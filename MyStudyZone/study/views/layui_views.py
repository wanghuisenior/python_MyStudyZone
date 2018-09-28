#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/20 8:15
"""
import json

from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from study import models
from study.models import User
from study.utils.LazyEncoder import LazyEncoder


def layui_home(request):
    return render(request, 'layui_home.html')


def layui_grid(request):
    return render(request, 'layui_grid.html')


def layui_button(request):
    return render(request, 'layui_button.html')


def layui_carousel(request):
    # 轮播组件
    return render(request, 'layui_carousel.html')


def layui_admin1(request):
    return render(request, 'layui_admin1.html')


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


def layui_index(request):
    # 表格
    return render(request, 'layui_index.html')


# admin后台框架
###########################################################3
def layui_login(request):
    return render(request, 'admin/login.html')


def layui_admin(request):
    return render(request, 'admin/layui_admin.html')


def layui_main(request):
    return render(request, 'admin/main.html')


def layui_admin_grid(request):
    return render(request, 'admin/layui_admin_grid.html')


def layui_admin_layer(request):
    return render(request, 'admin/layui_admin_layer.html')


def layui_admin_table(request):
    if request.GET:
        return_data = {}
        # for i in list(request.GET):
        #     page = json.loads(i)['page']
        #     limit = json.loads(i)['limit']
        print('GET请求内容:', request.GET)
        try:
            # page = request.GET['page'] if not None else 1  # 请求第几页的数据  !!!此处不能用get函数获取page不知道为什么
            # limit = request.GET['limit'] if not None else 10 # 该页有几条数据
            page = request.GET.get('page', 1)
            limit = request.GET.get('limit', 10)
            print(page, limit)
            export = request.GET.get('export', False)  # 当前是否为导出excel表的标志
            sort_key = request.GET.get('key', None)  # 点击表头上的排序，传递过来，根据哪个字段进行排序
            sort_order = request.GET.get('order', None)  # 排序方式，asc；desc
            print('请求页码', page, ';请求条数:', limit, ';是否导出:', export, ';排序字段:', sort_key, ';排序方式:', sort_order)
            print('***********************************************************************************************')
            users = models.User.objects.get_queryset().order_by('create_time')
            # 分页实现
            paginator = Paginator(users, limit)
            try:
                user_list = paginator.page(page).object_list
                print('分页成功')
            except PageNotAnInteger:
                user_list = paginator.page(1).object_list
                print('PageNotAnInteger')
            except EmptyPage:
                user_list = paginator.page(paginator.num_pages)
                print('EmptyPage')
            return_data['code'] = 0
            return_data['msg'] = '查询到了数据'
            return_data['count'] = len(users)
            return_data['data'] = list()
            for user in users if export else user_list:
                return_data['data'].append({'id': user.user_id, 'user_name': user.user_name, 'user_tel': user.user_tel,
                                            'user_email': user.user_email, 'create_time': user.create_time,
                                            'update_time': user.update_time, 'user_info': user.user_info})
        except User.DoesNotExist:
            return_data['code'] = 1
            return_data['msg'] = '出错啦'
        return HttpResponse(json.dumps(return_data, cls=LazyEncoder))
    else:
        return render(request, 'admin/layui_admin_table.html')
