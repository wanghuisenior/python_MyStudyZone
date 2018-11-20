#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/17 10:41
"""
import json
import time

import faker
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from study import models
from study.models import User
from study.utils.LazyEncoder import LazyEncoder


def index(request):
    return render(request, 'index.html')




def JTable_test(request):

    if request.GET:
        action = request.GET.get('action')
        if action == 'list':
            users = models.User.objects.all().order_by('create_time')
            # 分页处理
            jtStartIndex = int(request.GET.get('jtStartIndex'))
            jtPageSize = int(request.GET.get('jtPageSize'))

            paginator = Paginator(users, jtPageSize, 2)  # 每页jtPageSize条,少于两条则合并到上一页
            current_page = jtStartIndex / jtPageSize + 1
            print('总共数据量', paginator.count, '可分页数', paginator.num_pages, '当前页', current_page)
            try:
                paged_user_list = paginator.page(current_page)  # contacts为Page对象！
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                paged_user_list = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                paged_user_list = paginator.page(paginator.num_pages)

            user_data_list = []
            for user in paged_user_list:
                user_data_list.append(user.encode2json())
            # print(user_data_list)
            return HttpResponse(
                json.dumps({'Result': 'OK', 'Records': user_data_list, 'TotalRecordCount': paginator.count}, cls=LazyEncoder))
        elif action == 'delete':
            return_data = {}
            user_id = request.POST.get('user_id', None)
            if user_id:
                try:
                    models.User.objects.get(user_id=user_id).delete()
                    return_data['Result'] = 'OK'
                except User.DoesNotExist:
                    return_data['Result'] = 'ERROR'
                    return_data['Message'] = '用户不存在'
                except Exception as e:
                    return_data['Result'] = 'ERROR'
                    return_data['Message'] = '未知异常'
                return HttpResponse(json.dumps(return_data))
        elif action == 'update':
            user_id = request.POST.get('user_id', None)
            user_name = request.POST.get('user_name', None)
            user_tel = request.POST.get('user_tel', None)
            user_email = request.POST.get('user_email', None)
            user_info = request.POST.get('user_info', None)
            return_data = {}
            if user_id:
                try:
                    models.User.objects.filter(user_id=user_id).update(user_name=user_name, user_tel=user_tel, user_email=user_email,
                                                                       user_info=user_info)
                    return_data['Result'] = 'OK'
                except User.DoesNotExist:
                    return_data['Result'] = 'ERROR'
                    return_data['Message'] = '用户不存在'
                except Exception as e:
                    return_data['Result'] = 'ERROR'
                    return_data['Message'] = '未知异常'
                return HttpResponse(json.dumps(return_data))

    else:
        return render(request, 'JTable_test.html')


def jtable_test_user_available(request):
    valid = True if len(models.User.objects.filter(user_name=request.GET.get('fieldValue', None))) == 0 else False
    # 向服务器端传两个参数：fieldId,fieldValue，
    # 根据这两个参数实现判断逻辑，然后返回一个三元素的数组：元素ID、检查是否通过(true or false)、提示信息。
    # 注意，字符串需要使用双引号引起来。
    res = []
    if valid:
        res.append(request.GET.get('fieldId', None))
        res.append(True)
        # res.append('哈哈，可以使用了')
        res.append('')
    else:
        res.append(request.GET.get('fieldId', None))
        res.append(False)
        res.append('已存在了啊 啊')
    print(res)
    return HttpResponse(json.dumps(res))
