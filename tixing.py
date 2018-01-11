# -*- coding: utf-8 -*-
# python版本：2.7

import cPickle as P
import msgcenter
import wrlog
import mailsend
import webpost


# 普通提醒函数
def tixing(name):
    storedlist = []
    f = file(name, 'r')
    try:
        storedlist = P.load(f)
    except:
        pass
    f.close()
    if len(storedlist) != 0:
        [u, v, w, i, x] = msgcenter.readtime()
        for text in storedlist:
            if u == str(int(text[0:4])):
                if v == str(int(text[5:7])):
                    if w == str(int(text[8:10])):
                        print str(int(text[11:13]))
                        if i == str(int(text[11:13])):
                            if x == str(int(text[14:16])):
                                zlog = '提醒：' + text
                                wrlog.wrlog(zlog)
                                mailsend.send('提醒', str(text[17:]), '823480758@qq.com')
                                f = file(name, 'r')
                                st = P.load(f)
                                f.close()
                                for i in range(len(st)):
                                    if st[i] == text:
                                        del st[i]
                                        break
                                f = file(name, 'w')
                                P.dump(st, f)
                                f.close()
                                webpost.webpost(webpost.msgformat('tixing.data', 'zuoye.data'))
                # 调用方式
                # tixing(‘tixing.data’)


# 作业提醒函数即相比于普通提醒提前一天
def zuoyetixing(name):
    storedlist = []
    f = file(name, 'r')
    try:
        storedlist = P.load(f)
    except:
        pass
    f.close()
    if len(storedlist) != 0:
        [u, v, w, i, x] = msgcenter.readtime()
        for text in storedlist:
            print text
            if u == str(int(text[0:4])):
                if v == str(int(text[5:7])):
                    if w == str(int(text[8:10]) - 1):
                        if i == str(int(text[11:13])):
                            if x == str(int(text[14:16])):
                                zlog = '作业提醒：'+text
                                wrlog.wrlog(zlog)
                                mailsend.send('作业', str(text[17:]), '823480758@qq.com')
                                f = file(name, 'r')
                                st = P.load(f)
                                f.close()
                                for i in range(len(st)):
                                    if st[i] == text:
                                        del st[i]
                                        break
                                f = file(name, 'w')
                                P.dump(st, f)
                                f.close()
                                webpost.webpost(webpost.msgformat('tixing.data', 'zuoye.data'))
