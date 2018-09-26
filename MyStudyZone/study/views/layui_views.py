#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/20 8:15
"""
import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from study import models


def layui_home(request):
    return render(request, 'layui_home.html')


def layui_grid(request):
    return render(request, 'layui_grid.html')


def layui_button(request):
    return render(request, 'layui_button.html')


def layui_carousel(request):
    # 轮播组件
    return render(request, 'layui_carousel.html')


def layui_admin1(request):
    return render(request, 'layui_admin1.html')


def layui_code(request):
    # 代码修饰器
    return render(request, 'layui_code.html')


def layui_element(request):
    # 常用元素
    return render(request, 'layui_element.html')


def layui_form(request):
    # 表单
    return render(request, 'layui_form.html')


def layui_laydate(request):
    # 时间选择器
    return render(request, 'layui_laydate.html')


def layui_layedit(request):
    # 富文本编辑器
    return render(request, 'layui_layedit.html')


def layui_layer(request):
    # 弹出层
    return render(request, 'layui_layer.html')


def layui_laypage(request):
    # 分页
    return render(request, 'layui_laypage.html')


def layui_rate(request):
    # 评分
    return render(request, 'layui_rate.html')


def layui_responsive(request):
    # 评分
    return render(request, 'layui_responsive.html')


def layui_table(request):
    # 表格
    return render(request, 'layui_table.html')


def layui_tree(request):
    # 表格
    return render(request, 'layui_tree.html')


def layui_upload(request):
    # 表格
    return render(request, 'layui_upload.html')


def layui_util(request):
    # 表格
    return render(request, 'layui_util.html')


def layui_index(request):
    # 表格
    return render(request, 'layui_index.html')


# admin后台框架
###########################################################3
def layui_login(request):
    return render(request, 'admin/login.html')


def layui_admin(request):
    return render(request, 'admin/layui_admin.html')


def layui_main(request):
    return render(request, 'admin/main.html')


def layui_admin_grid(request):
    return render(request, 'admin/layui_admin_grid.html')


def layui_admin_table(request):
    print(request.GET)
    if request.GET:
        print('get不为空')
        users = models.User.objects.all()
        print(serializers.serialize('json', users))

        json = {
            "code": 0
            , "msg": ""
            , "count": 3000000
            , "data": [{
                "id": "10001"
                , "username": "杜甫"
                , "email": "xianxin@layui.com"
                , "sex": "男"
                , "city": "浙江杭州"
                , "sign": "点击此处，显示更多。当内容超出时，点击单元格会自动显示更多内容。"
                , "experience": "7"
                , "ip": "192.168.0.8"
                , "logins": 0
                , "joinTime": "2016-10-14"
            }, {
                "id": "10002"
                ,
                "username": "李白"
                ,
                "email": "xianxin@layui.com"
                ,
                "sex": "男"
                ,
                "city": "浙江杭州"
                ,
                "sign": "君不见，黄河之水天上来，奔流到海不复回。 君不见，高堂明镜悲白发，朝如青丝暮成雪。 人生得意须尽欢，莫使金樽空对月。 天生我材必有用，千金散尽还复来。 烹羊宰牛且为乐，会须一饮三百杯。 岑夫子，丹丘生，将进酒，杯莫停。 与君歌一曲，请君为我倾耳听。(倾耳听 一作：侧耳听) 钟鼓馔玉不足贵，但愿长醉不复醒。(不足贵 一作：何足贵；不复醒 一作：不愿醒/不用醒) 古来圣贤皆寂寞，惟有饮者留其名。(古来 一作：自古；惟 通：唯) 陈王昔时宴平乐，斗酒十千恣欢谑。 主人何为言少钱，径须沽取对君酌。 五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。"
                ,
                "experience": "9"
                ,
                "ip": "192.168.0.8"
                ,
                "logins": "106"
                ,
                "joinTime": "2016-10-14"
                ,
                "LAY_CHECKED": 'true'
            }, {
                "id": "10003"
                , "username": "王勃"
                , "email": "xianxin@layui.com"
                , "sex": "男"
                , "city": "浙江杭州"
                , "sign": "人生恰似一场修行"
                , "experience": "8"
                , "ip": "192.168.0.8"
                , "logins": "106"
                , "joinTime": "2016-10-14"
            }, {
                "id": "10004"
                , "username": "李清照"
                , "email": "xianxin@layui.com"
                , "sex": "女"
                , "city": "浙江杭州"
                , "sign": "人生恰似一场修行"
                , "experience": "6"
                , "ip": "192.168.0.8"
                , "logins": "106"
                , "joinTime": "2016-10-14"
            }, {
                "id": "10005"
                , "username": "冰心"
                , "email": "xianxin@layui.com"
                , "sex": "女"
                , "city": "浙江杭州"
                , "sign": "人生恰似一场修行"
                , "experience": "64"
                , "ip": "192.168.0.8"
                , "logins": "106"
                , "joinTime": "2016-10-14"
            }, {
                "id": "10006"
                , "username": "贤心"
                , "email": "xianxin@layui.com"
                , "sex": "男"
                , "city": "浙江杭州"
                , "sign": "人生恰似一场修行"
                , "experience": "65"
                , "ip": "192.168.0.8"
                , "logins": "106"
                , "joinTime": "2016-10-14"
            }, {
                "id": "10007"
                , "username": "贤心"
                , "email": "xianxin@layui.com"
                , "sex": "男"
                , "city": "浙江杭州"
                , "sign": "人生恰似一场修行"
                , "experience": "49"
                , "ip": "192.168.0.8"
                , "logins": "106"
                , "joinTime": "2016-10-14"
            }, {
                "id": "10008"
                , "username": "贤心"
                , "email": "xianxin@layui.com"
                , "sex": "男"
                , "city": "浙江杭州"
                , "sign": "人生恰似一场修行"
                , "experience": "5"
                , "ip": "192.168.0.8"
                , "logins": "106"
                , "joinTime": "2016-10-14"
            }]
        }
        return HttpResponse(json)
    # context = {'users': users}
    else:
        print('get空')
        return render(request, 'admin/layui_admin_table.html')
