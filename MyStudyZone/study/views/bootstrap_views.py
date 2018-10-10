#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/17 10:41
"""
import json
import uuid

from PIL import Image
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from study import models
from study.models import User
import datetime
from datetime import date

from study.utils.LazyEncoder import LazyEncoder


def index(request):
    return render(request, 'index.html')


def icons(request):
    return render(request, 'icons.html')


def bootstrap_grid(request):
    return render(request, 'bootstrap_grid.html')


def bootstrap_table(request):
    if request.method == 'GET':
        if request.GET:  # GET请求不为空
            user_filter = {}
            # user_filter['user_id'] = request.GET['user_id']
            users = User.objects.all().filter(user_name__contains=request.GET['user_name'])
            # user_list = []
            # for user in users:
            #     user_list.append(
            #         {'user_id': user.user_id, 'user_name': user.user_name, 'user_tel': user.user_tel,
            #          'user_email': user.user_email,
            #          'create_time': user.create_time})
            # return HttpResponse(json.dumps(user_list, cls=LazyEncoder))
            print(request.GET)
            return HttpResponse(serializers.serialize("json", users, cls=LazyEncoder))
        else:  # GET请求,请求内容为空，说明是点击跳转页面
            return render(request, 'bootstrap_table.html')


def del_users(request):
    res = dict()
    ids = request.POST.getlist('ids[]')
    try:
        for user_id in ids:
            models.User.objects.get(user_id=user_id).delete()
        res['is_success'] = True
    except User.DoesNotExist:
        res['is_success'] = False
        res['error_msg'] = '用户不存在'
    except Exception as e:
        res['is_success'] = False
        res['error_msg'] = e.message
    return HttpResponse(json.dumps(res))


def create_or_update_user(request):
    res = dict()
    user_id = request.POST.get('user_id')
    user_name = request.POST.get('user_name')
    user_tel = request.POST.get('user_tel')
    user_email = request.POST.get('user_email_header') + '@' + request.POST.get('user_email_footer')
    user_info = request.POST.get('user_info')
    ############################
    # 获取到上传的图片文件
    image = request.FILES.get('image')
    print(image.name, image.size)
    ############################
    try:
        if user_id:  # user_id不为空，修改数据
            user = models.User.objects.get(user_id=user_id)
        else:  # 添加数据
            user = User()
        user.user_name = user_name
        user.user_tel = user_tel
        user.user_email = user_email
        user.user_info = user_info
        if image:
            user.image = image
        user.save()
        res['is_success'] = True
    except User.DoesNotExist:
        res['is_success'] = False
        res['error_msg'] = '用户不存在'
    except Exception as e:
        res['is_success'] = False
        res['error_msg'] = e.message
    return HttpResponse(json.dumps(res))


def get_user_names(request):
    # bootstrap typeahead模糊查询
    # values 方法可以获取number字段的字典列表。
    # <QuerySet [{'user_name': 'aaa'}, {'user_name': 'aaaaaa'}, {'user_name': 'afdsaaaa'}]>

    # values_list 可以获取number的元组列表。
    # <QuerySet [('aaa',), ('aaaaaa',), ('afdsaaaa',)]>

    # values_list方法加个参数flat = True可以获取number的值列表。
    # < QuerySet['aaa', 'aaaaaa', 'afdsaaaa'] >
    names_queryset = models.User.objects.filter(
        user_name__contains=request.POST.get('param')).values_list('user_name', flat=True)
    return HttpResponse(json.dumps(list(names_queryset), cls=LazyEncoder))


def bootstrap_validator(request):
    return render(request, 'bootstrap_validator.html')


def bootstrap_navbar(request):
    return render(request, 'bootstrap_navbar.html')
