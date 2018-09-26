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
    # for i in range(101,500):
    #     models.User.objects.create(user_name='测试用户' + str(i), user_tel='1853082503' + str(i), user_email='test' + str(i) + '@qq.com')

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


def layui_admin_table(request):
    if request.GET:
        return_data = {}
        page, limit = 1, 10
        for i in list(request.GET):
            page = json.loads(i)['page']
            limit = json.loads(i)['limit']
        print('==', page, limit)
        try:
            users = models.User.objects.all()
            # 分页实现
            paginator = Paginator(users, limit)
            try:
                user_list = paginator.page(page).object_list
            except PageNotAnInteger:
                user_list = paginator.page(1).object_list
            except EmptyPage:
                user_list = paginator.page(paginator.num_pages)
            return_data['code'] = 0
            return_data['msg'] = '查询到了数据'
            return_data['count'] = len(users)
            return_data['data'] = list()
            for user in user_list:
                return_data['data'].append({'id': user.user_id, 'user_name': user.user_name, 'user_tel': user.user_tel,
                                            'user_email': user.user_email, 'create_time': user.create_time,
                                            'update_time': user.update_time, 'user_info': user.user_info})
        except User.DoesNotExist:
            return_data['code'] = 1
            return_data['msg'] = '出错啦'
        return HttpResponse(json.dumps(return_data, cls=LazyEncoder))
    else:
        print('get空')
        return render(request, 'admin/layui_admin_table.html')
