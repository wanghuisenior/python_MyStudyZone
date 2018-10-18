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
from study.utils.LazyEncoder import LazyEncoder


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
    try:
        image = request.FILES.get('image')
        print(image.name, image.size)
    except:
        pass
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


def update_user_info(request):
    print('update_user_info')
    try:
        user = models.User.objects.get(user_id=request.POST['user_id'])
        user.user_name = request.POST['user_name']
        user.save()
    except User.DoesNotExist:
        return HttpResponse(404)
    except Exception as e:
        return HttpResponse(json.dumps(e))
    return HttpResponse(200)
