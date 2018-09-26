#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/9/25 8:10
"""
import calendar
import datetime


class DateUtil(object):
    # 初始化函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Get date list from start_date to end_date
    @classmethod
    def get_date_list(cls, start_date, end_date):
        """
        传入开始日期和结束日期，返回中间所有的日期列表
        :param start_date:开始日期
        :param end_date:结束日期
        :return:
        """
        start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        dates = []
        while start <= end:
            dates.append(start.strftime('%Y-%m-%d'))
            start += datetime.timedelta(days=1)
        return dates

    @classmethod
    def get_month_list(cls, start_date, end_date):
        """
        获取月份列表
        :param start_date:
        :param end_date:
        :return:
        """
        date_list = []
        begin_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m")
            date_list.append(date_str)
            begin_date = add_months(begin_date, 1)
        return date_list

    @classmethod
    def get_day(cls, date_str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').day

    @classmethod
    def get_month(cls, date_str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').month

    @classmethod
    def get_year(cls, date_str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').year

    @classmethod
    def get_quarter_list(cls, start_date, end_date):
        """
        获取季度列表
        :param begin_date:
        :param end_date:
        :return:
        """
        quarter_list = []
        month_list = DateTool.get_month_list(start_date, end_date)
        for value in month_list:
            tempvalue = value.split("-")
            if tempvalue[1] in ['01', '02', '03']:
                quarter_list.append(tempvalue[0] + "Q1")
            elif tempvalue[1] in ['04', '05', '06']:
                quarter_list.append(tempvalue[0] + "Q2")
            elif tempvalue[1] in ['07', '08', '09']:
                quarter_list.append(tempvalue[0] + "Q3")
            elif tempvalue[1] in ['10', '11', '12']:
                quarter_list.append(tempvalue[0] + "Q4")
        quarter_set = set(quarter_list)
        quarter_list = list(quarter_set)
        quarter_list.sort()
        return quarter_list


def add_months(dt, months):
    month = dt.month - 1 + months
    year = dt.year + month // 12
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)
