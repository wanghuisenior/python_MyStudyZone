#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @author: 王辉
 @email: wanghui@zih718.com
 @time: 2018/8/23 11:01
"""
import itchat
import requests
from itchat.content import TEXT, PICTURE, RECORDING

KEY = 'ef7dc5a9ff924d2f8b254fd59737830a'


def get_response(msg):
    # 构造了要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        print('机器人回复:', r.get('text'))
        return '图灵智能机器人：' + r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        return '发生了意料之外的错误。'


# 注册后才能获取到微信消息
@itchat.msg_register(TEXT, PICTURE, RECORDING)
def tuling_reply(msg):
    my_username = itchat.get_friends(update=True)[0].UserName  ##获取自己的username
    my_nickname = itchat.get_friends(update=True)[0].NickName
    # print(my_username, my_nickname)
    my_all_friends = itchat.get_friends(update=True)
    for friend in my_all_friends:
        if friend.UserName == msg['FromUserName']:
            print('发送人：', friend.NickName, friend.RemarkName, ',内容：', msg['Text'])
    for friend in my_all_friends:
        if friend.UserName == msg['ToUserName']:
            print('接收人：', friend.NickName, friend.RemarkName)
    # if not msg['FromUserName'] == myUserName:  ###如果不是自己发的
    return get_response(msg['Text'])


# isGroupChat=True表示为群聊消息
@itchat.msg_register([TEXT, PICTURE, RECORDING], isGroupChat=True)
def group_reply_text(msg):
    # 消息来自于哪个群聊
    chatroom_id = msg['User']['UserName']
    # 发送者的昵称
    username = msg['ActualNickName']
    print('chatroom_id:', chatroom_id, 'username:', username)
    myUserName = itchat.get_friends(update=True)[0]["UserName"]  ##获取自己的username
    print('myUserName=', myUserName)
    print('FromUserName=', msg['FromUserName'])  ##获取发消息的好友的username
    remark_name = msg['User']['RemarkName']  ###备注名称
    username = msg['User']['NickName']
    print('username=', msg['User']['NickName'])
    # rooms = itchat.get_chatrooms(update=True)[0:]
    reply = remark_name + get_response(msg['Text'])
    print('question:', msg['Text'])
    print('reply:', reply)
    if chatroom_id != 'adc6286314e20fac2bb054163d3c704d1380dc1edf36b1e858ed508dc3614e69':
        itchat.send_msg(reply, toUserName=chatroom_id)


# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.run()
