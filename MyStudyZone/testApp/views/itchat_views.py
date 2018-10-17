#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/10/9 17:37
"""
import json

import itchat
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'itchat/itchat_index.html')


def wechat_login(request):
    itchat.auto_login(hotReload=True)  # 这里若抛出异常，把itchat.pkl删除再重新来一遍试试
    friends = itchat.get_friends(update=True)[1:]
    friend_list = []
    for item in friends:
        friend_list.append(
            {'NickName': item.NickName, 'RemarkName': item.RemarkName, 'Sex': '男' if item.Sex == 1 else '女' if item.Sex == 2 else '未指定',
             'Province': item.Province,
             'Signature': item.Signature})
    return HttpResponse(json.dumps(friend_list))
