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


def bootstrap_index(request):
    return render(request, 'bootstrap_admin/bootstrap_index.html')


def confirm_with_bs(request):
    return render(request, 'bootstrap_admin/confirm_with_bs.html')


def bootstrap_grid(request):
    return render(request, 'bootstrap_admin/bootstrap_grid.html')


def bootstrap_table(request):
    if request.method == 'GET':
        if request.GET:  # GET请求不为空
            user_filter = {}
            # user_filter['user_id'] = request.GET['user_id']
            users = User.objects.all().filter(user_name__contains=request.GET['user_name'])
            user_list = []
            for user in users:
                user_list.append(
                    {'user_id': user.user_id, 'user_name': user.user_name, 'user_tel': user.user_tel, 'user_email': user.user_email,
                     'image': user.image, 'user_info': user.user_info, 'create_time': user.create_time, 'update_time': user.update_time})
            return HttpResponse(json.dumps(user_list, cls=LazyEncoder))
            # print(request.GET)
            # return HttpResponse(serializers.serialize("json", users, cls=LazyEncoder))
        else:  # GET请求,请求内容为空，说明是点击跳转页面
            return render(request, 'bootstrap_admin/bootstrap_table.html')


def bootstrap_validator(request):
    return render(request, 'bootstrap_admin/bootstrap_validator.html')


def bootstrap_table_edit(request):
    if request.method == 'GET':
        if request.GET:  # get请求不为空
            print('get请求不为空', request.GET)
            users = models.User.objects.all()
            user_list = []
            for user in users:
                user_list.append(
                    {'user_id': user.user_id, 'user_name': user.user_name, 'user_tel': user.user_tel, 'user_email': user.user_email,
                     'image': user.image, 'user_info': user.user_info, 'create_time': user.create_time, 'update_time': user.update_time})
            return HttpResponse(json.dumps(user_list, cls=LazyEncoder))
        else:
            print('get请求空')
            return render(request, 'bootstrap_admin/bootstrap_table_edit.html')
