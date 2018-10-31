#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/10/26 9:14
"""


# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("参数没有包含数字\n", Argument)


# 调用函数
temp_convert("xyz")
