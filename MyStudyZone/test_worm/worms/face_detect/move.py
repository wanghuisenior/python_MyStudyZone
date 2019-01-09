#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName: 捕获摄像头.py
 @Author: 王辉/Administrator
 @Email: wanghui@zih718.com
 @Date: 2019/1/8 17:12
 @Description:
"""
import time

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5))
# 获取摄像头返回的宽和高
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# 确定保存视频的格式
name = './' + time.strftime("%Y%m%d_%H_%M_%S", time.localtime(time.time())) + '.avi'
video = cv2.VideoWriter(name, fourcc, 5, size)

pre_frame = None  # 总是取前一帧做为背景（不用考虑环境影响）
while 1:
	ret, cur_frame = cap.read()
	# show a frame
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray_img = cv2.cvtColor(cur_frame, cv2.COLOR_BGR2GRAY)
	# gray_img = cv2.resize(gray_img, (500, 500))
	# gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
	cv2.imshow("capture", gray_img)
	if pre_frame is None:
		pre_frame = gray_img
	else:
		img_delta = cv2.absdiff(pre_frame, gray_img)
		thresh = cv2.threshold(img_delta, 25, 255, cv2.THRESH_BINARY)[1]
		thresh = cv2.dilate(thresh, None, iterations=2)
		image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		for c in contours:
			if cv2.contourArea(c) < 1000:  # 设置敏感度
				continue
			else:
				# print(cv2.contourArea(c))
				print("前一帧和当前帧不一样了, 有什么东西在动!")
				video.write(cur_frame)  # 写入视频文件，此处不写入也能实时显示
				break

		pre_frame = gray_img

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
