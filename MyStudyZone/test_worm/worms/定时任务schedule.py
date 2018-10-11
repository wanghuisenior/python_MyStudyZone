#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/10/11 16:00
"""
import schedule


def task():
    print('test')


schedule.every(3).seconds.do(task)

while True:
    schedule.run_pending()
