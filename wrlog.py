# -*- coding: utf-8 -*-
# python版本： 2.7

import datetime


# 与此动作的发生时间与记录一起写入日志文件
def wrlog(text):
    f = open('log.txt', 'a')
    log = '\n' + str(datetime.datetime.now()) + '\n'
    f.write(log)
    f.write(text)
    f.close()
    print '写入日志成功...'
