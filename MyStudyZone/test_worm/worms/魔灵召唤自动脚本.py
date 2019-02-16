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
# EXECUTE_TIME = 20  # 执行次数
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TIME_HUOSHAN = 80  # 火山  +10秒 随机
TIME_LONG = 80  # 龙  +10秒 随机
TIME_JUREN = 100  # 巨人 +10秒 随机
TIME_MOLI = 120  # 魔力 +10秒 随机
TIME_SHUI = 110  # 水 +10秒 随机
TIME_HUO = 110  # 火 +10秒 随机
TIME_FENG = 120  # 风 +10秒 随机
TIME_GUANG = 110  # 光 +10秒 随机
TIME_AN = 110  # 暗 +10秒 随机
# 4分45秒增加一点体力，, 再减去点击按钮所消耗的12秒，读条也需要时间
TIME_ONCE = 6  # 一次副本需要消耗6点体力
TIME_FOREVER = (60 * 4 + 45) * TIME_ONCE - 12  # +10秒随机   刷一次副本所需的时间  刚好和新产生的体力数量差不多，这样可以一直不停的刷下去
# TIME_FOREVER = 10
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
if not config.has_section('ready'):
	print('检测到未配置【战斗准备】按钮位置，即将开始进行配置...')
	time.sleep(2)
	config.add_section('ready')
	print('请将鼠标移至【战斗准备】按钮左侧...')
	for x in range(5, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
		if x == 0:
			print('\r成功记录鼠标位置...', mouse.position())
			config.set('ready', 'left', str(mouse.position()))
	print('请将鼠标移至【战斗准备】按钮上方...')
	for x in range(5, -1, -1):
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
		if x == 0:
			print('\r成功记录鼠标位置...', mouse.position())
			config.set('ready', 'top', str(mouse.position()))
config.write(open(config_file_name, 'w', encoding='utf8'))


############################

def execute_task(sleep_time, current, execute_time):
	if execute_time:
		print('\r开始执行第%s次任务...共需执行%s次' % (current + 1, execute_time))
	else:
		print('\r开始执行第%s次任务...' % (current + 1))
	print('\r点击[再来一次]按钮', end='', flush=True)
	mouse.click(start_again_left[0] + random.randint(0, start_again_right[0] - start_again_left[0]),
				start_again_left[1] - 5 + random.randint(0, 10))
	time.sleep(3)
	# ======================>>
	for x in range(sleep_time, -1, -1):
		# 这里是副本过程
		print('\r倒计时{0}'.format(x), end='', flush=True)
		time.sleep(1)
	# 倒计时结束，点击两下屏幕，获取结果
	# =======================>>
	confirm_btn_center_x = (confirm_left[0] + confirm_right[0]) // 2
	print('\r点击[空白处]显示宝箱', end='', flush=True)
	mouse.click(confirm_btn_center_x - 5 + random.randint(0, ready_left[0] - confirm_btn_center_x),
				ready_top[1] + 20 - random.randint(0, 40))
	time.sleep(3)
	print('\r点击[空白处]打开宝箱', end='', flush=True)
	mouse.click(confirm_btn_center_x - 5 + random.randint(0, ready_left[0] - confirm_btn_center_x),
				ready_top[1] + 20 - random.randint(0, 40))
	time.sleep(3)
	print('\r点击[确认]按钮', end='', flush=True)
	mouse.click(confirm_btn_center_x - 5 + random.randint(0, ready_left[0] - confirm_btn_center_x),
				ready_top[1] + 20 - random.randint(0, 40))
	time.sleep(3)
	print('\r点击[获得道具]按钮', end='', flush=True)
	mouse.click(ready_left[0] - random.randint(5, 15), ready_left[1])
	current += 1


###########################
TIME_HUOSHAN = 80  # 火山  +10秒 随机
TIME_JUREN = 100  # 巨人 +10秒 随机
TIME_LONG = 80  # 龙  +10秒 随机
TIME_MOLI = 110  # 魔力 +10秒 随机
TIME_SHUI = 110  # 水 +10秒 随机
TIME_HUO = 110  # 火 +10秒 随机
TIME_FENG = 110  # 风 +10秒 随机
TIME_GUANG = 110  # 光 +10秒 随机
TIME_AN = 110  # 暗 +10秒 随机
flag = input('请输入 1:火山 2: 巨人 3: 龙 4:魔力 5: 水 \n 6: 火 7:风 8: 光 9: 暗 0：不停刷 \n')
try:
	flag = int(flag)
	if not (
			flag == 1 or flag == 2 or flag == 3 or flag == 4 or flag == 5 or flag == 6 or flag == 7 or flag == 8 or flag == 9 or flag == 0):
		print('数据有误，请输入合法的整数')
		exit(0)
except ValueError:
	print('数据有误，请输入合法的整数')
	exit(0)

ready_left = eval(config['ready']['left'])
ready_top = eval(config['ready']['top'])
start_again_left = eval(config['start_again']['left'])
start_again_right = eval(config['start_again']['right'])
confirm_left = eval(config['confirm']['left'])
confirm_right = eval(config['confirm']['right'])

if flag == 0:
	# 产生体力所需的时间  和  打副本消耗的时间  一致  即可保存一直有充足的体力
	current = 0
	while 1:
		execute_task(TIME_FOREVER, current, None)
		current += 1
else:
	execute_time = input('请输入执行次数\n')
	try:
		execute_time = int(execute_time)
	except ValueError:
		print('数据有误，执行次数必须为正整数')
		exit(0)
	sleep_time = 0
	for i in range(execute_time):
		if flag == 1:
			sleep_time = TIME_HUOSHAN
		elif flag == 2:
			sleep_time = TIME_JUREN
		elif flag == 3:
			sleep_time = TIME_LONG
		elif flag == 4:
			sleep_time = TIME_MOLI
		elif flag == 5:
			sleep_time = TIME_SHUI
		elif flag == 6:
			sleep_time = TIME_HUO
		elif flag == 7:
			sleep_time = TIME_FENG
		elif flag == 8:
			sleep_time = TIME_GUANG
		elif flag == 9:
			sleep_time = TIME_AN
		elif flag == 0:
			sleep_time = TIME_FOREVER
		sleep_time += random.randint(0, 10)
		execute_task(sleep_time, i, execute_time)
