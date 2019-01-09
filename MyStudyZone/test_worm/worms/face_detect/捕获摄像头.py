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


def Contrast_and_Brightness(alpha, beta, img):
	# 其中alpha调节对比度， beta调节亮度
	blank = np.zeros(img.shape, img.dtype)
	# dst = alpha * img + beta * blank
	dst = cv2.addWeighted(img, alpha, blank, 1 - alpha, beta)
	return dst

cap = cv2.VideoCapture(0)
while 1:
	ret, frame = cap.read()
	# show a frame
	cv2.imshow("capture", Contrast_and_Brightness(1.3, 1, frame))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
