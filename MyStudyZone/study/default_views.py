#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/17 10:41
"""
from django.http import HttpResponse
from django.shortcuts import render

from study import models


def href(request):
    return render(request, 'href.html')


def db_test_add(request):
    for i in range(1000):
        models.User.objects.create(user_name=str(i), user_tel='1853082503' + str(i),
                                   user_email='test' + str(i) + '@qq.com',
                                   user_info='我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名我的个性签名' + str(
                                       i))
    return HttpResponse('添加数据成功')


def test(request):
    return render(request, 'admin/onelevel.html')
