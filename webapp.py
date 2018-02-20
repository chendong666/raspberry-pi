# -*- coding:utf-8 -*-
# A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
# return 'Hello from Flask!'

import hashlib
import xml.etree.ElementTree as ET
from flask import Flask, request
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.debug = True

tixingxinxi = '未读取'
cc = ['a']


@app.route('/', methods=['GET', 'POST'])
def haha():
    if request.method == 'GET':
        token = 'ChenDong6DF5'  # 微信配置所需的token
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        s = ''.join(sorted([timestamp, nonce, token]))
        sha1 = hashlib.sha1()
        sha1.update(bytes(s))
        if sha1.hexdigest() == signature:
            return echostr
    else:
        xml = ET.fromstring(request.data)
        toUser = xml.find('ToUserName').text
        fromUser = xml.find('FromUserName').text
        msgType = xml.find("MsgType").text
        createTime = xml.find("CreateTime")
        if msgType == "text":
            content = xml.find('Content').text
            if content != '查询':
                global cc
                cc.append(content)
                return reply_text(fromUser, toUser, reply(fromUser, '操作完成'))
            elif content == '查询':
                global tixingxinxi
                return reply_text(fromUser, toUser, reply(fromUser, tixingxinxi))
        else:
            return reply_text(fromUser, toUser, "我只懂文字")


@app.route("/ok")
def ok():
    global cc
    aa = cc
    cc = ['a']
    return ' '.join(aa)


@app.route('/fasong', methods=['POST'])
def jishou():
    global tixingxinxi
    tixingxinxi = request.form['tixingxinxi']
    return 'ok'


def reply_text(to_user, from_user, content):
    """
    以文本类型的方式回复请求
    :param to_user:
    :param from_user:
    :param content:
    :return:
    """

    return """
    <xml>
        <ToUserName><![CDATA[{}]]></ToUserName>
        <FromUserName><![CDATA[{}]]></FromUserName>
        <CreateTime>{}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{}]]></Content>
    </xml>
    """.format(to_user, from_user,
               int(time.time() * 1000), content)


def reply(openid, msg):
    # 简单地翻转一下字符串就回复用户
    return msg


if __name__ == '__main__':
    app.run()
