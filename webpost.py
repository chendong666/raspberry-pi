# -*- coding:utf-8 -*-

import urllib
import urllib2
import cPickle as P


# 将信息发送到服务器端的函数
def webpost(msg):
    url = "http://chendong.pythonanywhere.com/fasong"
    postDict = {
        'tixingxinxi': msg,
    }
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    postData = urllib.urlencode(postDict)
    request = urllib2.Request(url, data=postData)
    backaa = opener.open(request).read()
    print u'信息返回至云端成功...'


# 获取手机发送至微信后台服务器的信息
def getmsg():
    a = urllib2.urlopen('http://chendong.pythonanywhere.com/ok').read().encode('utf-8')
    return a


# 将发送到服务器的函数进行格式化
def msgformat(file1, file2):
    fanhuixinxi = '提醒：'
    for name in [file1, file2]:
        f = file(name, 'r')
        x = P.load(f)
        f.close()
        if name == file2:
            fanhuixinxi = fanhuixinxi + '\n' + '作业：'
        for aa in x:
            fanhuixinxi = fanhuixinxi + '\n' + aa
    return fanhuixinxi

