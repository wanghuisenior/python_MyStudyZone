#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/17 10:41
"""
from django.shortcuts import render


def href(request):
    return render(request, 'href.html')


def test(request):
    return None
