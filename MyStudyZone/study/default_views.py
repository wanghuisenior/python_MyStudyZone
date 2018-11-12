#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/17 10:41
"""
import time

from django.http import HttpResponse
from django.shortcuts import render

from study import models


def index(request):
    return render(request, 'index.html')


def db_test_add(request):
    for i in range(1000):
        models.User.objects.create(user_name=str(i), user_tel='1853082503' + str(i),
                                   user_email='test' + str(i) + '@qq.com',
                                   user_info='我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名' + str(
                                       i))
    return HttpResponse('添加数据成功')


def test(request):
    return render(request, 'layui_admin/onelevel.html')


def jquery_util_test(request):
    return render(request, 'jquery_util_test.html')


def jquery_util_ajx_test(request):
    time.sleep(2) #Python time sleep() 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。

    return HttpResponse('我是通过后台加载到的数据')
