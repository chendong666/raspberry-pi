# -*- coding: utf-8 -*-
# python版本：2.7

import xlrd
import wrlog
import datetime
import cPickle as P


# 根据weeks文件返回今天是多少周
def getnowweek(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    a = {}
    for i in range(21):
        keys = int(float(table.cell(i, 0).value))
        c = []
        for j in range(1, 8):
            # 这样做去除周数中有小数的情况
            b = str(table.cell(i, j).value)
            c.append(b)
        a[keys] = c
    i = datetime.datetime.now().month
    j = datetime.datetime.now().day
    nowd = str(i) + '.' + str(j)
    for key in a.keys():
        if nowd in a[key]:
            nowweek = key
    return '第' + str(nowweek) + '周'


# 读取class.xls并创建一个class.data文件
def readclass(xlsname):
    data = xlrd.open_workbook(xlsname)
    table = data.sheets()[0]
    a = {}
    for i in range(6):
        for j in range(7):
            b = table.cell(i, j).value
            if b == 0:
                continue
            else:
                a[(i, j)] = b
    # 返回一个含课表的字典，字典的键为一个星期代码和节数代码，值为课程详情的字典，没有课的则不再字典内
    shoplistfile = 'class.data'
    f = file(shoplistfile, 'w')
    P.dump(a, f)
    f.close()
    wrlog.wrlog('提取信息创建class.data完成')


def getclass(filename, massage):
    print massage
    f = file(filename, 'r')
    a = P.load(f)
    f.close()
    week = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    dama = {0: '第一二节', 1: '第三四节', 2: '第五六节', 3: '第七八节', 4: '第九十节', 5: '第十一节'}
    cc = ''
    c = datetime.datetime.now().weekday()
    for j in range(6):
        if (j, c) in a.keys():

            if int(massage[3:-3]) in week[int(a[(j, c)][-18:-16]):int(a[(j, c)][-15:-13]) + 1]:
                if int(massage[3:-3]) - 2 * (int(massage[3:-3]) / 2) == int(a[(j, c)][-11]):
                    cc = cc + dama[j] + a[(j, c)][:-19] + a[(j, c)][-10:] + '\n'
                elif int(a[(j, c)][-11]) == 3:
                    cc = cc + dama[j] + a[(j, c)][:-19] + a[(j, c)][-10:] + '\n'
    wrlog.wrlog('解析当天课程完成')
    return cc


def creatnew():
    ff = []
    f = file('tixing.data', 'w')
    P.dump(ff, f)
    f.close()
    f = file('zuoye.data', 'w')
    P.dump(ff, f)
    f.close()


def readtime():
    u = str(int(datetime.datetime.now().year))
    v = str(int(datetime.datetime.now().month))
    w = str(int(datetime.datetime.now().day))
    i = datetime.datetime.now().hour
    x = datetime.datetime.now().minute
    # s = datetime.datetime.now().second
    return [u, v, w, i, x]


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
