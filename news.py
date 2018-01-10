# -*- coding: utf-8 -*-
# python版本：2.7

import urllib2
from bs4 import BeautifulSoup

# 解析网页
def main():
    a = urllib2.urlopen('http://news.baidu.com/').read()
    soup = BeautifulSoup(a, 'html.parser')
    links = soup.find_all('div', id="left-col-wrapper")
    c = links[0].find_all('a', target="_blank")
    d = []
    for i in range(0, len(c)):
        d.append(c[i].get_text())
        d.append(c[i].get('href'))
    x = ''
    for i in d:
        x = x + i +'\n'
    return x

# 防止网页解析出错
def news():
    try:
        try:
            return main()
        except:
            try:
                return main()
            except:
                try:
                    return main()
                except:
                    try:
                        return main()
                    except:
                        try:
                            return main()
                        except:
                            return main()
    except:
        return ' '

