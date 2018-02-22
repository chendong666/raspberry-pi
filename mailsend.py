# -*- coding:utf-8 -*-
# python 版本2.7.13

import wrlog
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send(head, message, mailadress):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header(head, 'utf-8')
    msg['From'] = Header('m17854119196@sina.com')
    msg['To'] = Header('receiver', 'utf-8')

    from_addr = 'm17854119196@sina.com'  # 发件邮箱
    password = 'wowangle123'  # 邮箱密码
    to_addr = mailadress  # 收件邮箱

    smtp_server = 'smtp.sina.com'  # SMTP服务器，以新浪为例

    try:
        server = smtplib.SMTP(smtp_server, 25)  # 第二个参数为默认端口为25，有些邮件有特殊端口

        server.login(from_addr, password)  # 登录邮箱
        server.sendmail(from_addr, to_addr, msg.as_string())  # 将msg转化成string发出
        server.quit()
        wrlog.wrlog("邮件发送成功")
        print '邮件发送成功'
    except smtplib.SMTPException as e:
        print '邮件发送失败', e
        wrlog.wrlog("邮件发送失败")
