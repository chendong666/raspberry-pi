# -*- coding: utf-8 -*-
# python版本：2.7

# 引入模块
import cPickle as P
import wrlog


# 修改暂时用删除后添加的方式解决
# 提醒信息修改函数
def xiugai(text):
    # 用格式化的字符串来输入修改那个文件及修改形式
    # 输入文本格式0-0-2018-1-01-01-12-00-提醒信息
    if int(text[2]) == 0:
        filename = 'tixing.data'
    elif int(text[2]) == 1:
        filename = 'zuoye.data'

    if int(text[0]) == 0:
        # 添加
        f = file(filename, 'r')
        tlist = P.load(f)
        f.close()
        # 写入data文件的格式是列表
        # 内部提醒信息格式修改为2018-01-01-12-00-提醒信息
        tlist.append(text[4:])
        f = file(filename, 'w')
        P.dump(tlist, f)
        f.close()
    if int(text[0]) == 1:
        # 删除
        f = file(filename, 'r')
        tlist = P.load(f)
        f.close()
        for i in range(len(tlist)):
            if tlist[i] == text[4:]:
                del tlist[i]
        f = file(filename, 'w')
        P.dump(tlist, f)
        f.close()
    wrlog.wrlog('修改作业提醒信息成功')