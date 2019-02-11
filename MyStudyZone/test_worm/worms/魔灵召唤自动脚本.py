#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName: 魔灵召唤自动脚本.py
 @Author: 王辉/Administrator
 @Email: wanghui@zih718.com
 @Date: 2019-02-11 9:49
 @Description:
 1 根据python版本下载对应版本的pyhook，并pip install pyHook-1.5.1-cp37-cp37m-win_amd64.whl
 https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook
 2 由于python3把pymouse和pykeyboard放在了pyuserinput这个包里面，所以我们只要安装这个包就可以了
 pip install pyuserinput
"""
import configparser
import random
import time

from pymouse import PyMouse

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
EXECUTE_TIME = 10  # 执行次数
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TIME_HUOSHAN = 6  # 火山  +10秒 随机
TIME_JUREN = 100  # 巨人 +10秒 随机
TIME_MOLI = 111  # 魔力 +10秒 随机
mouse = PyMouse()
config_file_name = 'play.txt'
config = configparser.ConfigParser()
config.read(config_file_name)
if not config.has_section('start_again'):
	print('检测到未配置【再来一次】按钮位置，即将开始进行配置...')
	time.sleep(2)
	config.add_section('start_again')
	print('请将鼠标移至【再来一次】按钮左侧...')
	for x in range(5, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
		if x == 0:
			print('\r成功记录鼠标位置...', mouse.position())
			config.set('start_again', 'left', str(mouse.position()))
	print('请将鼠标移至【再来一次】按钮右侧...')
	for x in range(5, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
		if x == 0:
			print('\r成功记录鼠标位置...', mouse.position())
			config.set('start_again', 'right', str(mouse.position()))
if not config.has_section('confirm'):
	print('检测到未配置【确认】按钮位置，即将开始进行配置...')
	time.sleep(2)
	config.add_section('confirm')
	print('请将鼠标移至【确认】按钮左侧...')
	for x in range(5, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
		if x == 0:
			print('\r成功记录鼠标位置...', mouse.position())
			config.set('confirm', 'left', str(mouse.position()))
	print('请将鼠标移至【确认】按钮右侧...')
	for x in range(5, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
		if x == 0:
			print('\r成功记录鼠标位置...', mouse.position())
			config.set('confirm', 'right', str(mouse.position()))
if not config.has_section('get_prop'):
	print('检测到未配置【获得道具】按钮位置，即将开始进行配置...')
	time.sleep(2)
	config.add_section('get_prop')
	print('请将鼠标移至【获得道具】按钮左侧...')
	for x in range(5, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
		if x == 0:
			print('\r成功记录鼠标位置...', mouse.position())
			config.set('get_prop', 'left', str(mouse.position()))
	print('请将鼠标移至【获得道具】按钮右侧...')
	for x in range(5, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
		if x == 0:
			print('\r成功记录鼠标位置...', mouse.position())
			config.set('get_prop', 'right', str(mouse.position()))
config.write(open(config_file_name, 'w', encoding='utf8'))
###########################
flag = input('请输入 1:自动火山 2: 自动巨人 3: 自动魔力\n')
try:
	flag = int(flag)
	if not (flag == 1 or flag == 2 or flag == 3):
		print('数据有误，请输入合法的整数')
		exit(0)
except ValueError:
	print('数据有误，请输入合法的整数')
	exit(0)
get_prop_left = eval(config['get_prop']['left'])
get_prop_right = eval(config['get_prop']['right'])
start_again_left = eval(config['start_again']['left'])
start_again_right = eval(config['start_again']['right'])
confirm_left = eval(config['confirm']['left'])
confirm_right = eval(config['confirm']['right'])
for i in range(EXECUTE_TIME):  # 这里填入执行次数
	sleep_time = TIME_HUOSHAN if flag == 1 else TIME_JUREN if flag == 2 else TIME_MOLI if flag == 3 else print('无效数据')
	sleep_time = sleep_time + random.randint(0, 10)
	print('\r开始执行第%s次任务...' % (i + 1))
	print('\r点击[再来一次]按钮', end='', flush=True)
	mouse.click(start_again_left[0] + random.randint(0, start_again_right[0] - start_again_left[0]),
				start_again_left[1] - 5 + random.randint(0, 5))
	for x in range(sleep_time, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
	# 倒计时结束，点击两下屏幕，获取结果
	print('\r点击[空白处]显示宝箱', end='', flush=True)
	mouse.click(confirm_left[0] + random.randint(0, confirm_right[0] - confirm_left[0]),
				confirm_left[1] - 5 + random.randint(0, 5))
	time.sleep(2)
	print('\r点击[空白处]打开宝箱', end='', flush=True)
	mouse.click(confirm_left[0] + random.randint(0, confirm_right[0] - confirm_left[0]),
				confirm_left[1] - 5 + random.randint(0, 5))
	time.sleep(2)
	print('\r点击[确认]按钮', end='', flush=True)
	mouse.click(confirm_left[0], confirm_left[1])
	time.sleep(2)
	print('\r点击[获得道具]按钮', end='', flush=True)
	mouse.click(get_prop_left[0] + random.randint(0, get_prop_right[0] - get_prop_left[0]),
				get_prop_left[1] - 5 + random.randint(0, 5))
	time.sleep(2)
print('\r任务执行完毕')
