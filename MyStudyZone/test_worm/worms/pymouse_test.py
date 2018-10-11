#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/10/11 8:17
"""
# 由于python3把pymouse和pykeyboard放在了pyuserinput这个包里面，所以我们只要安装这个包就可以了
# 如果直接pip install pyuserinput，会提示要先安装pyhook这个包。
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook
from pymouse import PyMouse

mouse = PyMouse()
x_dim, y_dim = mouse.screen_size()
print('屏幕大小', x_dim, y_dim)
print('鼠标现在所在位置', mouse.position())
print('屏幕正中央位置', int(x_dim / 2), int(y_dim / 2))
mouse.move(int(x_dim / 2), int(y_dim / 2))  # 鼠标移动到屏幕正中央

mouse.click(int(x_dim / 2), int(y_dim / 2))

mouse.click(int(x_dim / 2), int(y_dim / 2), 1 | 2)  # 移动并且在xy位置点击,左右键点击1是点击的鼠标左键,2是右键,3是中建。
