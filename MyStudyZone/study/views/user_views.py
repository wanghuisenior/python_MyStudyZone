#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/25 10:15
"""
from django.shortcuts import render, redirect

from study import models


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
    models.User.objects.all().filter(user_id=user_id).delete()
    return redirect(user_manage)
