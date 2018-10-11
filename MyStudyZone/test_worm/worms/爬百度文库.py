#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/8/23 10:12
"""
import requests
import re
import json
import os

session = requests.session()


def fetch_url(url):
    return session.get(url).content.decode('gbk')


def get_doc_id(url):
    return re.findall('view/(.*).html', url)[0]


def parse_type(content):
    return re.findall(r"docType.*?\:.*?\'(.*?)\'\,", content)[0]


def parse_title(content):
    return re.findall(r"title.*?\:.*?\'(.*?)\'\,", content)[0]


def parse_doc(content):
    result = ''
    url_list = re.findall('(https.*?0.json.*?)\\\\x22}', content)
    url_list = [addr.replace("\\\\\\/", "/") for addr in url_list]
    for url in url_list[:-5]:
        content = fetch_url(url)
        y = 0
        txtlists = re.findall('"c":"(.*?)".*?"y":(.*?),', content)
        for item in txtlists:
            if not y == item[1]:
                y = item[1]
                n = '\n'
            else:
                n = ''
            result += n
            print(result)
            result += item[0].encode('utf-8').decode('unicode_escape', 'ignore')
    return result


def parse_txt(doc_id):
    content_url = 'https://wenku.baidu.com/api/doc/getdocinfo?callback=cb&doc_id=' + doc_id
    content = fetch_url(content_url)
    md5 = re.findall('"md5sum":"(.*?)"', content)[0]
    pn = re.findall('"totalPageNum":"(.*?)"', content)[0]
    rsign = re.findall('"rsign":"(.*?)"', content)[0]
    content_url = 'https://wkretype.bdimg.com/retype/text/' + doc_id + '?rn=' + pn + '&type=txt' + md5 + '&rsign=' + rsign
    content = json.loads(fetch_url(content_url))
    result = ''
    for item in content:
        for i in item['parags']:
            result += i['c'].replace('\\r', '\r').replace('\\n', '\n')
    return result


def parse_other(doc_id):
    content_url = "https://wenku.baidu.com/browse/getbcsurl?doc_id=" + doc_id + "&pn=1&rn=99999&type=ppt"
    content = fetch_url(content_url)
    url_list = re.findall('{"zoom":"(.*?)","page"', content)
    # url_list = [item.replace("\", '') for item in url_list]
    if not os.path.exists(doc_id):
        os.mkdir(doc_id)
    for index, url in enumerate(url_list):
        content = session.get(url).content
    path = os.path.join(doc_id, str(index) + '.jpg')
    with open(path, 'wb') as f:
        f.write(content)
    print("图片保存在" + doc_id + "文件夹")


def save_file(filename, content):
    with open(filename, 'w', encoding='utf8') as f:
        f.write(content)
        print('已保存为:' + filename)


def main():
    url = input('请输入要下载的文库URL地址_')
    content = fetch_url(url)
    doc_id = get_doc_id(url)
    type = parse_type(content)
    title = parse_title(content)
    if type == 'doc':
        result = parse_doc(content)
        save_file(title + '.txt', result)
    elif type == 'txt':
        result = parse_txt(doc_id)
        save_file(title + '.txt', result)
    else:
        parse_other(doc_id)


if __name__ == "__main__":
    main()
