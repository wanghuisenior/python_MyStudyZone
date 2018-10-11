#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/8/7 17:35
"""
import json
import random
import string

import requests
from bs4 import BeautifulSoup

# response = requests.get('https://blog.csdn.net/kikaylee/article/details/56841789')
# print(response.status_code)  # 打印状态码
# print(response.url)  # 打印请求url
# print(response.headers)  # 打印头信息
# print(response.cookies)  # 打印cookie信息
# print(response.text)  # 以文本形式打印网页源码
# print(response.content)  # 以字节流形式打印
# bs = BeautifulSoup(response.text.encode('utf-8'))
# print(bs.prettify())
# 类型,,top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
params = {'type': '', 'key': '635bfc1b134d22fe67f08306a022e3c0'}
response = requests.get('http://v.juhe.cn/toutiao/index', params=params)
print(response.text)
print(response.json())
# result = json.loads(response.text)
result = response.json().get('result')
if result:
    data_list = result.get('data')
    print(len(data_list))
    # for data in data_list:
    #     print(data)


