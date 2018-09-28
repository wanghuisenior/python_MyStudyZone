#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/25 10:15
"""
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from study import models
from study.models import User


def user_manage(request):
    users = models.User.objects.all()
    content = {'users': users}
    return render(request, 'user/user_manage.html', content)


def search(request):
    users = models.User.objects.all().filter(user_name__contains=request.GET['user_name'])
    content = {'users': users}
    return render(request, 'user/user_manage.html', content)


def get_user_by_id(request, user_id):
    users = models.User.objects.all().filter(user_id=user_id)

    content = {'users': users}
    return render(request, 'user/user_manage.html', content)


def delete_user_by_id(request, user_id):
    print(user_id)
    models.User.objects.all().filter(user_id=user_id).delete()
    return redirect(user_manage)


def delete_user_by_id1(request):
    print('delete_user_by_id1', request.GET)
    return_data = {}
    try:
        for user_id in request.GET.getlist('user_id_list[]'):
            models.User.objects.all().get(user_id=user_id).delete()
        return_data['code'] = 200
    except User.DoesNotExist:
        return_data['code'] = 1
    print(return_data)
    return HttpResponse(json.dumps(return_data))
