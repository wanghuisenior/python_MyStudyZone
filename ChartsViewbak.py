# coding=utf8
import datetime
import io
import json

import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import escape_uri_path

from zih import models
from zih.models import ZihAmount
from zih.models import ZihAmountclientname, Organization
from zih.utils.tools import DateTool


def fullload_rate(request):
    """
    满载率/重箱  图表
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "fullload_rate.html")
    elif request.method == "POST":
        start = request.POST.get("start_date")
        end = request.POST.get("end_date")
        line = request.POST.get("line")
        # groupby = request.POST.get("groupby")
        groupby = ''
        dateKey_list = DateTool.get_month_list(start, end) if groupby == '0' else DateTool.get_date_list(start, end)
        # 获取条件下order_number不重复的对象集合
        qc_distinct_datas = get_distinct_data_by_ordernumber(None, line, 0, None, start, end)
        hc_distinct_datas = get_distinct_data_by_ordernumber(None, line, 1, None, start, end)
        # print(len(hc_distinct_datas))
        qucheng_data_list = get_date_sum_list(qc_distinct_datas, dateKey_list, groupby)
        huicheng_data_list = get_date_sum_list(hc_distinct_datas, dateKey_list, groupby)
        return HttpResponse(json.dumps([qucheng_data_list, huicheng_data_list]))


def get_date_sum_list(distinct_datas, dateKey_list, groupby):
    """
    满载率/重箱图表， 获取到数据
    :param dateKey_list:
    :param distinct_datas:
    :param groupby:
    :return:
    """
    date_code_dic = {}
    # for data in temp_datas.values():
    #     date_key = data.class_date.strftime('%Y-%m-%d')
    #     date_code_dic[date_key] = []
    for date in dateKey_list:
        date_code_dic[date] = []
    for data in distinct_datas:  # temp_datas.values():这是上面取出的ordernumber不重复的对象集合（使用了字典的特性）
        date_key = data.class_date.strftime('%Y-%m') if groupby == '0' else data.class_date.strftime('%Y-%m-%d')
        container_boxamount = data.container_boxamount
        container_type = data.container_type
        banlie_code = data.banlie_code
        if data.container_type and container_boxamount != 0:  # 班列类型不为空且包含“20尺”字符串的为半个箱
            real_container_boxamount = container_boxamount * 0.5 if "20尺" in container_type else container_boxamount
            # print(date_key, banlie_code, real_container_boxamount)
            date_code_dic[date_key].append({banlie_code: real_container_boxamount})
            # date_code_dic[date_key].append({banlie_code: data.order_number + ':' + str(real_container_boxamount)})
    return_data = {}
    # print('date_code_dic', date_code_dic)
    for date in date_code_dic:
        code_sum = {}
        for code_amount in date_code_dic[date]:
            # print('num', code_amount)
            for code in code_amount:
                amount = code_amount[code]
                if 'P' in code:
                    if 'PA' in code:
                        code = code[:-1]
                    else:
                        pass
                    if code in code_sum.keys():
                        code_sum[code] += amount
                    else:
                        code_sum[code] = amount
                else:
                    if 'A' in code:
                        code = code[:-1]
                    else:
                        pass
                    if code in code_sum.keys():
                        code_sum[code] += amount
                    else:
                        code_sum[code] = amount
        return_data[date] = code_sum
    return return_data


def volume_analysis(request):
    """
    亚欧部上货量图表
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "volume_analysis.html")
    elif request.method == "POST":
        line = request.POST.get("line")
        quhui = request.POST.get("param1")
        zhengpin = request.POST.get("param2")
        s_date = request.POST.get("s_date")
        e_date = request.POST.get("e_date")
        user_info = request.session.get('user_info', None)
        # ************************* 部门集合*****************************#
        level1 = {}
        level2 = {}
        tzb = {}
        level3 = {}
        jylevel4 = {}
        jyblevel4code = {}
        tzb_tjr = {}
        codeset = Organization.objects.filter(Organization_Code__istartswith='YWB')
        for ywb in codeset:
            if len(ywb.Organization_Code) == 9:
                level1[ywb.Organization_Code] = ywb.Organization_Name[0:4]
            if len(ywb.Organization_Code) == 12:
                level2[ywb.Organization_Code] = ywb.Organization_Name
                for t_tz in list(level2.items()):
                    if '经营' == t_tz[1][0:2]:
                        level2[t_tz[0]] = t_tz[1][0:4]
            if len(ywb.Organization_Code) == 15:
                level3[ywb.Organization_Code] = ywb.Organization_Name
            if len(ywb.Organization_Code) == 17:
                jylevel4[ywb.Organization_Code] = ywb.Organization_Name
                jyblevel4code[ywb.Organization_Code[0:15]] = ywb.Organization_Name
        # ************************* 标准推荐人集合*****************************#
        standard_referee_dic = {}
        referee_list = models.Referee.objects.filter(referee_org_code__istartswith='YWB').filter(
            referee_name__isnull=False)
        for referee in referee_list:
            code = referee.referee_org_code
            name = referee.referee_name

            if len(code) <= 15:  # 所有长度小于等于15的，不要；  但 ‘张 耘 硕’ 是特例 ，他长度15的有值，长度大于15的没值,
                # if name == '张 耘 硕':
                if code == 'YWB100101100101':  # 这个值不过滤，（这样取出的推荐人集合中，此人有两个code，其中长度大于15的没值）
                    pass
                else:
                    continue
            if code in standard_referee_dic.keys():
                if name not in standard_referee_dic[code]:
                    standard_referee_dic[code].append(name)
            else:
                standard_referee_dic[code] = []
        # print(standard_referee_dic)
        for ttt in list(standard_referee_dic.items()):
            for zzz in list(tzb.items()):
                if ttt[0][0:15] == zzz[0]:
                    tzb_tjr[zzz[1]] = ttt[1]

        zuizhongbumen = dict(level1, **level2, **level3, **jylevel4)
        objects = get_distinct_data_by_ordernumber(user_info['ywbcode'], line, quhui, zhengpin, s_date, e_date)
        temp = {}
        for obj in objects:
            day_key = obj.class_date.strftime('%Y-%m-%d')
            day_value = float(
                obj.px_settlement_volume if obj.px_settlement_volume is not None else 0) if zhengpin == '1' else (
                obj.container_boxamount * 0.5 if '20尺' in obj.container_type else obj.container_boxamount)

            for referee_code in standard_referee_dic:
                if obj.organization_code.startswith(referee_code):
                    list_referee_names = standard_referee_dic[referee_code]  # 这里取出标准推荐人集合中的推荐人
                    for name in list_referee_names:
                        if obj.yw_name == name:
                            single_data = {obj.yw_name: {day_key: day_value}}

                            if obj.organization_code in temp.keys():
                                temp[obj.organization_code].append(single_data)
                            else:
                                temp[obj.organization_code] = [single_data]
        new_data = {}
        for code in temp:
            all_day_data = {}  # 包含所有日期，若该日期没有数据则设置其上货量为0
            # 创建模板，每天为0
            for name_day_amount_dic in temp[code]:
                for name in name_day_amount_dic:
                    for d in DateTool.get_date_list(s_date, e_date):
                        if name not in all_day_data.keys():
                            all_day_data[name] = {d: 0}
                        else:
                            all_day_data[name][d] = 0
            # 数据中该日期上货量不为0的加上去
            for name_day_amount_dic in temp[code]:
                for name in name_day_amount_dic:
                    for day_k in name_day_amount_dic[name]:
                        all_day_data[name][day_k] += name_day_amount_dic[name][day_k]
                        new_data[code] = all_day_data
        # print(new_data)
        test = {}
        for code in new_data:
            level1_code = code[0:9]
            level2_code = code[0:12]
            level3_code = code[0:17] if code[0:15] in jyblevel4code.keys() else code[0:15]
            level1_name = zuizhongbumen[level1_code]
            level2_name = zuizhongbumen[level2_code]
            level3_name = zuizhongbumen[level3_code]
            if level1_name in test.keys():
                if level2_name in test[level1_name].keys():
                    if level3_name in test[level1_name][level2_name].keys():
                        test[level1_name][level2_name][level3_name].append(new_data[code])
                    else:
                        test[level1_name][level2_name][level3_name] = [new_data[code]]
                else:
                    test[level1_name][level2_name] = {level3_name: [new_data[code]]}
            else:
                test[level1_name] = {level2_name: {level3_name: [new_data[code]]}}
        print(test['亚欧二部'])
        return HttpResponse(json.dumps(test))


def get_distinct_data_by_ordernumber(org_code, line, quhui, zhengpin, s_date, e_date):
    """
    获取筛选条件下，所有order_number不重复的ZihAmount objects集合
    :param line:
    :param org_code:
    :param quhui:
    :param zhengpin:
    :param s_date:
    :param e_date:
    :return:
    """
    data_filter = {}
    if org_code is not None and org_code != '':
        data_filter['organization_code__startswith'] = org_code
    if line is not None and line != '':
        data_filter['typeid'] = line
    if quhui is not None and quhui != '':
        data_filter['quhui'] = quhui
    if zhengpin is not None and zhengpin != '':
        data_filter['zhengpin'] = zhengpin
    data_filter['class_date__range'] = [s_date, e_date]
    data_list = ZihAmount.objects.all().filter(**data_filter).exclude(organization_code__icontains='KX')
    distinct_order_number_list = data_list.values('order_number').distinct()
    temp_datas = {}
    for item in distinct_order_number_list:
        temp_datas[item.get('order_number')] = 0
    for data in data_list:
        temp_datas[data.order_number] = data  # 这里一个ordernumber可能对应多个container_boxamount相同的对象，我只取最后一个
    return temp_datas.values()


def get_clientdate(req):
    # print("start=================================", req.path)
    all_data = []
    if req.method == "POST":
        # print("keywords====", req.POST)
        line = req.POST.get('param0')
        quhui = req.POST.get("param1")
        zhengpin = req.POST.get("param2")
        sdate = req.POST.get("s_date")
        edate = req.POST.get("e_date")
        ywbname = req.session.get('user_info')['department_name']
        ywbcode = req.session.get('user_info')['ywbcode']

        filter = {}
        if line != '':
            filter['typeid'] = line
        if quhui != "":
            filter['quhui'] = quhui
        if zhengpin != "":
            filter['zhengpin'] = zhengpin
        if sdate != "" and edate != "":
            filter['class_date__range'] = [sdate, edate]

        filterparam = ZihAmountclientname.objects.exclude(order_number__contains='PX'). \
            filter(organization_code__startswith=ywbcode).exclude(organization_code__icontains='KX').filter(**filter)
        ############################################################################

        distinct_queryset = filterparam.values('order_number').distinct()
        distinct_list = {}
        for i in distinct_queryset:
            distinct_list[i['order_number']] = None
        for data in filterparam:
            distinct_list[data.order_number] = data
        data_list = distinct_list.values()  # 不重复的 order_number数据集
        # print('去重后', len(data_list))

        dic = {}
        for data in data_list:
            dic[data.client_name] = 0
        for data in data_list:
            if zhengpin == '0':
                if data.container_boxamount:
                    if "20尺" in data.container_type:
                        dic[data.client_name] += 0.5 * data.container_boxamount
                    else:
                        dic[data.client_name] += data.container_boxamount
            else:
                if data.px_settlement_volume:
                    dic[data.client_name] += float(data.px_settlement_volume)
        for k, v in dic.items():
            dic[k] = round(v, 2)

        # *********************************piedata*********************************************#

        top10 = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:10]
        elseclient = sorted(dic.items(), key=lambda x: x[1], reverse=True)[10:]
        sum = 0
        for i in elseclient:
            sum += float(i[1])
        top10.append(('其他', round(sum, 2)))
        all_data.append(top10)

        # ***********************************linedata************************************************ #
        valuetemp = {}
        for item in top10[0:10]:
            clidic = {}  ##ordernumber 与 classdate 对应
            ocli = {}
            valuetemp[item[0]] = 0
            datas = filterparam.filter(client_name=item[0]).values('order_number').distinct()
            for data in filterparam:
                ocli[data.class_date.strftime('%Y-%m-%d')] = 0
            for data in datas:
                tempid = data['order_number']
                clidic[tempid] = 0
            for i in data_list:
                client_order_id = i.order_number
                timeid = i.class_date.strftime('%Y-%m-%d')
                zx = i.container_boxamount
                px = i.px_settlement_volume
                type = i.container_type
                if client_order_id in clidic.keys():
                    if zhengpin == '0':
                        if timeid in ocli.keys():
                            if "20尺" in type:
                                ocli[timeid] += 0.5 * zx
                            else:
                                ocli[timeid] += zx
                        else:
                            ocli[timeid] = zx

                    elif px is not None:
                        if timeid in ocli.keys():
                            ocli[timeid] += float(px)
                        else:
                            ocli[timeid] = float(px)
                else:
                    pass
            for k, v in ocli.items():
                ocli[k] = round(v, 2)
            # print("================", item[0], ocli)
            valuetemp[item[0]] = ocli
        all_data.append([valuetemp])
        if len(ywbcode) > 6:
            all_data.append(ywbname)
        else:
            all_data.append('班列业务部')
        return HttpResponse(json.dumps(all_data))
    return render(req, "client_chart.html")


def dingcangclient(req):
    # print("start================", req.path)
    if req.method == 'POST':
        # print("keyword========", req.POST)
        line = req.POST.get('param0')
        quhui = req.POST.get("param1")
        zhengpin = req.POST.get("param2")
        sdate = req.POST.get("s_date")
        edate = req.POST.get("e_date")
        c_name = req.POST.get("paramclient")
        flag = req.POST.get("flag")
        filter = {}
        if line != '':
            filter['typeid'] = line
        if quhui != "":
            filter['quhui'] = quhui
        if zhengpin != "":
            filter['zhengpin'] = zhengpin
        if sdate != "" and edate != "":
            filter['class_date__range'] = [sdate, edate]
        if c_name != "":
            filter['client_name'] = c_name

        filterset = ZihAmountclientname.objects.exclude(order_number__contains='PX') \
            .exclude(organization_code__icontains='KX').filter(**filter)

        distinct_queryset = filterset.values('order_number').distinct()
        # print('num=', distinct_queryset)
        order_number_list = {}
        clientdata = {}
        for i in distinct_queryset:
            order_number_list[i['order_number']] = None
        for data in filterset:
            order_number_list[data.order_number] = data
        data_list = order_number_list.values()
        for i in data_list:
            timeid = i.class_date.strftime('%Y-%m-%d')
            zx = i.container_boxamount
            px = i.px_settlement_volume
            type = i.container_type
            if zhengpin == '0':
                if timeid in clientdata.keys():
                    if "20尺" in type:
                        clientdata[timeid] += 0.5 * zx
                    else:
                        clientdata[timeid] += zx
                else:
                    clientdata[timeid] = zx
            elif px is not None:
                if timeid in clientdata.keys():
                    clientdata[timeid] += float(px)
                else:
                    clientdata[timeid] = float(px)

        return HttpResponse(json.dumps(clientdata))
    return render(req, "dingcang_client.html")


def download_client_excel(req):
    quhui = req.POST.get("quhui")
    zhengpin = req.POST.get("zhengpin")
    s_date = req.POST.get("s_date")
    e_date = req.POST.get("e_date")
    client_name = req.POST.get("client_name")
    filter = {}
    if quhui != "":
        filter['quhui'] = quhui
    if zhengpin != "":
        filter['zhengpin'] = zhengpin
    if s_date != "" and e_date != "":
        filter['class_date__range'] = [s_date, e_date]
    if client_name != "":
        filter['client_name'] = client_name

    filterset = ZihAmountclientname.objects.exclude(order_number__contains='PX') \
        .exclude(organization_code__icontains='KX').filter(**filter)

    distinct_queryset = filterset.values('order_number').distinct()
    # print('num=', distinct_queryset)
    order_number_list = {}
    clientdata = {}
    for i in distinct_queryset:
        order_number_list[i['order_number']] = None
    for data in filterset:
        order_number_list[data.order_number] = data
        clientdata[data.class_date.strftime('%Y-%m-%d')] = 0

    data_list = order_number_list.values()
    for i in data_list:
        timeid = i.class_date.strftime('%Y-%m-%d')
        zx = i.container_boxamount
        px = i.px_settlement_volume
        type = i.container_type
        if zhengpin == '0':
            if timeid in clientdata.keys():
                if "20尺" in type:
                    clientdata[timeid] += 0.5 * zx
                else:
                    clientdata[timeid] += zx
        elif px is not None:
            if timeid in clientdata.keys():
                clientdata[timeid] += float(px)
            else:
                clientdata[timeid] = float(px)
    header = ['客户名称']
    datas = [client_name]
    for day in clientdata:
        header.append(datetime.datetime.strptime(day, '%Y-%m-%d').strftime('%m-%d'))
        datas.append(clientdata[day])
    return write_excel(client_name, datas, header)


def set_style(font_name, height, bold=False):
    """
    设置单元格样式
    :param font_name:
    :param height:
    :param bold:
    :return:
    """
    style = xlwt.XFStyle()  # 初始化样式
    al = xlwt.Alignment()
    al.horz = 0x02  # 设置水平居中
    al.vert = 0x01  # 设置垂直居中
    style.alignment = al
    font = xlwt.Font()  # 为样式创建字体
    font.name = font_name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 000
    font.height = height
    style.font = font
    # alignment = style.alignment #对齐
    # alignment.HORZ_CENTER

    # 设置单元格边框
    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6
    # style.borders = borders

    # 设置单元格背景颜色
    # pattern = xlwt.Pattern()
    # 设置其模式为实型
    # pattern.pattern = pattern.SOLID_PATTERN
    # 设置单元格背景颜色
    # pattern.pattern_fore_colour = 0x00
    # style.pattern = pattern

    return style


def get_client_names(request):
    name_str = request.POST.get('name')
    clients = models.Client.objects.filter(client_name__contains=name_str)
    names = []
    for client in clients:
        names.append({client.id: client.client_name})
    return HttpResponse(json.dumps(names))


def write_excel(file_name, data, header):
    if not file_name:
        file_name = '未指定'
    # 打开一个Excel工作簿
    file = xlwt.Workbook()
    # 新建一个sheet，如果对一个单元格重复操作，会引发异常，所以加上参数cell_overwrite_ok=True
    sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)
    if data is None:
        return file
    # 写标题栏
    # row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计']
    # for i in range(0, len(row0)):
    #     sheet1.write_merge(0, 0, i, i, row0[i], set_style('Times New Roman', 220, True))
    #     sheet1.write_merge(0, 2, 7, 9, "单元格合并", set_style('Times New Roman', 220, True))
    """
    table.write_merge(x, x + m, y, w + n, string, sytle)
    x表示行，y表示列，m表示跨行个数，n表示跨列个数，string表示要写入的单元格内容，
    style表示单元格样式。其中，x，y，w，n，都是以0开始计算的。
    """
    # l = 0
    # n = len(header)
    # # 写入数据
    for i in range(0, len(data)):
        sheet1.write(0, i, header[i], set_style('Times New Roman', 220, True))
        sheet1.write(1, i, data[i])
    # 直接保存文件
    # file.save("excel_name.xls")
    # 写入IO
    res = get_excel_stream(file)
    # 设置HttpResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    # response['Content-Disposition'] = 'attachment;filename={0}'.format(file_name) + '.xls'
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name)) + '.xls'
    # 将文件流写入到response返回
    response.write(res)
    return response


def get_excel_stream(file):
    # StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
    excel_stream = io.BytesIO()
    # 这点很重要，传给save函数的不是保存文件名，而是一个BytesIO流（在内存中读写）
    file.save(excel_stream)
    # getvalue方法用于获得写入后的byte将结果返回给re
    res = excel_stream.getvalue()
    excel_stream.close()
    return res
