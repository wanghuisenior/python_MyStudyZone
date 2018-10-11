#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/10/11 16:00
"""
import time

import schedule


def task():
    print('test')
    time.sleep(2)


schedule.every(3).seconds.do(task)

while True:
    schedule.run_pending()
