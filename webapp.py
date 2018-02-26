# -*- coding:utf-8 -*-
# A very simple Flask Hello World app for you to get started with...

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
# return 'Hello from Flask!'
import sys
import time
import hashlib
from flask import Flask, request
import xml.etree.ElementTree as ET

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.debug = True

tixingxinxi = '未读取'
msglist = ['a']
weizhi = []


@app.route('/', methods=['GET', 'POST'])
def mainfunc():
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
        # createTime = xml.find("CreateTime")
        if msgType == "text":
            content = xml.find('Content').text
            if content != '查询':
                global msglist
                msglist.append(content)
                return reply_text(fromUser, toUser, '操作完成')
            elif content == '查询':
                global tixingxinxi
                return reply_text(fromUser, toUser, tixingxinxi)
        elif msgType == 'image':
            imageurl = xml.find('PicUrl').text
            return reply_text(fromUser, toUser, imageurl)
        elif msgType == 'voice':
            yuyinxiaoxi = xml.find('Recognition').text
            msglist.append(yuyinxiaoxi)
            return reply_text(fromUser, toUser, yuyinxiaoxi)
        elif msgType == 'location':
            global weizhi
            weizhi.append(xml.find('Label').text)
            weizhi.append(xml.find('Location_X').text)
            weizhi.append(xml.find('Location_Y').text)
            fanhui = ','.join(weizhi)
            return reply_text(fromUser, toUser, fanhui)


@app.route("/jieshou")
def jieshoutixing():
    global msglist
    fanhui = msglist
    msglist = ['a']
    return ' '.join(fanhui)

@app.route("/jieshou/location")
def jieshoulocation():
    global weizhi
    fanhui = ','.join(weizhi)
    return fanhui


@app.route('/fasong', methods=['POST'])
def jishou():
    global tixingxinxi
    tixingxinxi = request.form['tixingxinxi']
    return '接收成功'


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
    """.format(to_user, from_user, int(time.time() * 1000), content)

if __name__ == '__main__':
    app.run()
