# -*- coding: utf-8 -*-
# python版本： 2.7

import datetime

# 带时间写入普通日志
def wrlog(text):
    f = open('log.txt', 'a')
    log = '\n' + str(datetime.datetime.now()) + '\n'
    f.write(log)
    f.write(text)
    f.close()