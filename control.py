# -*- coding: utf-8 -*-
# python版本：2.7

# 引入邮箱发送模块
import mailsend
# 引入天气处理模块
import weather
# 两封不同邮箱地址的邮件发送提供时间间隔以及运行停顿
import time
# 创建新的data文件以及读取xls文件创建data文件用以配置提醒以及读取当前周的信息以及读取其他信息
import readmsg
# 提供提醒的函数
import tixing
# 爬取新闻
import news
# 引入日志
import wrlog
# 用以从服务器端接收提醒命令以及发送提醒列表
import webpost
# 用以接收服务端提醒命令后将其加入配置文件
import xiugai

# 在树莓派中要加入
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 引入日志文件
# ！！！正式运行时将此处删除即可wrlog函数内部为附加写模式，没有log文件会自动创建
# 此处代码为了清除之前的日志，正式运行删掉以保留较长时间的日志用以优化
f = open('log.txt', 'w')
f.close()
wrlog.wrlog('程序启动')

# 设定时间
seth = 23
setm = 27
# 城市代码（济南）
city = 'CN101120101'
# 空气检测点
station = '长清党校'

emailadress1 = '603333924@qq.com'
emailadress2 = '823480758@qq.com'

readmsg.readclass('class.xls')
try:
    webpost.webpost(webpost.msgformat('tixing.data', 'zuoye.data'))
    wrlog.wrlog('读取原有信息成功')
except:
    readmsg.creatnew()
    webpost.webpost('未读取')
    wrlog.wrlog('创建新的data文件完成')
j = 0

a = webpost.getmsg().split()
if len(a) > 1:
    wrlog.wrlog('云端数据读取成功')
    a = a[1:]
    for aa in a:
        xiugai.xiugai(aa)
else:
    wrlog.wrlog('无云端数据')
while True:
    [u, v, w, i, x] = readmsg.readtime()
    tixing.tixing('tixing.data')
    tixing.zuoyetixing('zuoye.data')
    if i == seth and x == setm and j == 0:
        massage3 = readmsg.getnowweek('week.xls')
        wrlog.wrlog('读取当前周完成')
        massage4 = readmsg.getclass('class.data', massage3)
        wrlog.wrlog('读取当天课表完成')
        # 获取天气信息
        massage1 = weather.main(city, station)
        # 想要不同城市修改此处
        massage2 = str(massage1) + '\n' + str(massage3) + '\n' + str(massage4) + '\n' + str(news.news())
        wrlog.wrlog('读取天气与新闻完成')
        # 将天气信息发送至指定邮箱
        # mailsend.send(massage1,emailadress1)
        # time.sleep(5)
        mailsend.send('早上好~', massage2, emailadress2)
        j = j + 1
    if i != seth and x != setm:
        j = 0
    time.sleep(3)
    a = webpost.getmsg().split()
    if len(a) > 1:
        wrlog.wrlog('云端数据读取成功')
        a = a[1:]
        for aa in a:
            xiugai.xiugai(aa)
        webpost.webpost(webpost.msgformat('tixing.data', 'zuoye.data'))
        wrlog.wrlog('提醒信息发送至云端成功')
