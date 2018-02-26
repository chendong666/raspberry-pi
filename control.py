# -*- coding: utf-8 -*-
# python版本：2.7

# 引入邮箱发送模块
import mailsend
# 处理天气与新闻信息
import morningmsg
# 在邮件发送间提供时间间隔以及运行停顿以节约性能
import time
# 主要信息、文件处理模块
import msgcenter
# 提供提醒的函数
import tixing
# 引入日志
import wrlog
# 用以从服务器端接收提醒命令以及发送提醒列表
import webpost

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
seth = '22'
setm = '31'
# 城市代码（济南）
city = 'CN101120101'
# 空气检测点
station = '长清党校'

emailadress1 = '6@qq.com'
emailadress2 = '823480758@qq.com'

msgcenter.readclass('class.xls')
try:
    webpost.webpost(webpost.msgformat('tixing.data', 'zuoye.data'))
    wrlog.wrlog('读取原有信息成功')
except:
    msgcenter.creatnew()
    webpost.webpost('未读取')
    wrlog.wrlog('创建新的data文件完成')
j = 0

a = webpost.getmsg()
if len(a) > 0:
    wrlog.wrlog('云端数据读取成功')
    print '获取云端信息成功...'
    for aa in a:
        if aa[0] in ['0','1']:
            msgcenter.xiugai(aa)
    webpost.webpost(webpost.msgformat('tixing.data', 'zuoye.data'))
    wrlog.wrlog('提醒信息发送至云端成功')
else:
    wrlog.wrlog('无云端数据')

while True:
    [u, v, w, i, x] = msgcenter.readtime()
    tixing.tixing('tixing.data')
    tixing.zuoyetixing('zuoye.data')
    if i == seth and x == setm and j == 0:
        massage3 = msgcenter.getnowweek('week.xls')
        wrlog.wrlog('读取当前周完成')
        massage4 = msgcenter.getclass('class.data', massage3)
        wrlog.wrlog('读取当天课表完成')
        # 获取天气信息
        massage1 = morningmsg.main()
        # 想要不同城市修改此处
        massage2 = str(massage1) + '\n' + str('第20周') + '\n' + \
            str(massage4)
        # 字符太长邮件会无法接受
        wrlog.wrlog('读取天气与新闻完成')
        # 将天气信息发送至指定邮箱
        # mailsend.send(massage1,emailadress1)
        # time.sleep(5)
        mailsend.send('早上好~', massage2, emailadress2)
        j = j + 1
    if i != seth and x != setm:
        j = 0
    time.sleep(3)
    a = webpost.getmsg()
    if len(a) > 0:
        wrlog.wrlog('云端数据读取成功')
        print '获取云端信息成功...'
        for aa in a:
            if aa[0] in ['0','1']:
                msgcenter.xiugai(aa)
        webpost.webpost(webpost.msgformat('tixing.data', 'zuoye.data'))
        wrlog.wrlog('提醒信息发送至云端成功')
