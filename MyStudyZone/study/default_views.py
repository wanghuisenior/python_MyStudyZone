#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/17 10:41
"""
import json
import time
from datetime import datetime

import faker
from django.contrib.sessions.models import Session
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render

from study import models
from study.models import User
from study.utils.LazyEncoder import LazyEncoder
from dwebsocket.decorators import accept_websocket

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
				json.dumps({'Result': 'OK', 'Records': user_data_list, 'TotalRecordCount': paginator.count},
						   cls=LazyEncoder))
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
					models.User.objects.filter(user_id=user_id).update(user_name=user_name, user_tel=user_tel,
																	   user_email=user_email,
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


def jquery_datatables_test(request):
	return render(request, 'DataTables_test.html')


def jquery_datatables_getdata(request):
	# page_size = request.GET.get('length', 10)  # 每页有多少条
	# offset = request.GET.get('start', 0)  # 数据偏移量
	# search_key = request.GET.get('search[value]', '')  # 搜索框内容
	# order_column = request.GET.get('order_column_index', '')  # 表示第几列需要排序
	# order_by = request.GET.get('order[0][dir]', '')  # 排序方式
	# current_page = int(offset) / int(page_size) + 1  # 当前请求的页码
	#
	#
	current_page = request.GET.get('current_page', 1)  # 当前请求的页码
	limit = request.GET.get('limit', 10)  # 每页有多少条
	search_keyword = request.GET.get('search_keyword', '')  # 搜索框内容
	order_column = request.GET.get('order_column', None)  # 表示第几列需要排序
	order_dir = request.GET.get('order_dir', '')  # 排序方式
	print('current_page:', current_page, 'limit:', limit, 'search_keyword:', search_keyword, 'order_column:',
		  order_column, 'order_dir:', order_dir)
	#
	#
	users = models.User.objects.all()
	if search_keyword:  # 合并查询结果，
		users = users.filter(user_name__icontains=search_keyword) | users.filter(
			user_tel__icontains=search_keyword) | users.filter(user_email__icontains=search_keyword) | users.filter(
			user_info__icontains=search_keyword)
	if order_column:  # 默认按照最近更新时间排序
		order_column = '-' + order_column if order_dir == 'desc' else order_column
		if order_column != 'user_id':  # model中默认已经按照update_time进行排序，所以不需要再排序
			users = users.order_by(order_column)
	user_list = list()
	for user in users:
		user_list.append({
			'user_id': user.user_id,
			'user_name': user.user_name,
			'user_tel': user.user_tel,
			'user_email': user.user_email,
			'user_info': user.user_info,
			'create_time': user.create_time,
			'update_time': user.update_time
		})
	paginator = Paginator(user_list, limit, 2)  # 创建分页对象,每页pagesize条数据,少于2条则合并到上一页显示(参数3)
	try:
		data_list = paginator.page(current_page).object_list  # 获取到当前页码的数据
		print('分页成功')
	except PageNotAnInteger:
		data_list = paginator.page(1).object_list
		print('PageNotAnInteger')
	except EmptyPage:
		data_list = paginator.page(paginator.num_pages)
		print('EmptyPage')
	return_data = {}
	return_data['recordsTotal'] = paginator.count
	return_data['recordsFiltered'] = paginator.count
	return_data['data'] = data_list
	print('在' < '给')
	return HttpResponse(json.dumps(return_data, cls=LazyEncoder))


def search_style(request):
	return render(request, 'search_style.html')


def wx_login(request):
	return render(request, 'wx_login.html')


def get_all_login_user():
	SQL = """
              SELECT  * FROM `django_session` WHERE expire_date >= NOW() GROUP BY session_data; 
              """
	# 根据session值是否重复判断用户是否在线  不太完善
	# sessions = Session.objects.filter(expire_date__gte=datetime.now())
	sessions = Session.objects.all()
	user_list = []
	# 获取session中的用户id
	for session in sessions:
		data = session.get_decoded()
		print(data)
		user_list.append(data.get('_auth_user_id', None))
	print(user_list, 66666666)
	return user_list


@accept_websocket
def get_user_list(request):
	if request.is_websocket():
		message = request.websocket.wait()
		print(message)
		while True:
			if message:
				user_list = get_all_login_user()
				# request.websocket.send(str(len(user_list)))
				request.websocket.send(str(11))
				time.sleep(10)
