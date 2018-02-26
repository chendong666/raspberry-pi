# -*-coding:utf-8-*-
# python版本 2.7

import json
import urllib
import urllib2
import datetime
from bs4 import BeautifulSoup


# 获取天气的类
class Weather(object):
    # 初始化函数直接获取天气状况json
    def __init__(self, url, city, key):
        # 编码网址信息
        self.msg = ''
        massage = {}
        # 在和风天气注册后获得的key
        massage['key'] = key
        massage['location'] = city
        urldata = urllib.urlencode(massage)
        encodeurl = url + urldata
        # 获取当前天气信息json
        w_html = urllib2.urlopen(encodeurl).read()
        self.w_json = json.loads(w_html)

    def get_weathermsg(self):
        databasic = self.w_json['HeWeather6'][0]['basic']
        for i in [0, 1, 2]:
            dataft = self.w_json['HeWeather6'][0]['daily_forecast'][i]
            if str(dataft['date'].encode('utf-8')[-2:]) == str(
                    datetime.datetime.now().day):
                break
        # 解析json格式化输出当前天气信息
        city = '城市:\t%s' % (databasic['location'].encode('utf-8'))
        date = '日期：\t%s' % (dataft['date'].encode('utf-8'))
        weather = '天气:\t%s' % (dataft['cond_txt_d'].encode('utf-8'))
        tmp = '温度:\t%s-%s度' % (dataft['tmp_min'].encode('utf-8'),
                               dataft['tmp_max'].encode('utf-8'))
        hum = '相对湿度(%):\t' + '%s' % (dataft['hum'].encode('utf-8'))
        wind = '风向(风力):\t%s(%s)' % (dataft['wind_dir'].encode('utf-8'),
                                    dataft['wind_sc'].encode('utf-8'))
        vis = '能见度:\t%skm' % (dataft['vis'].encode('utf-8'))
        pcpn = '降水量:\t\t%smm' % (dataft['pcpn'].encode('utf-8'))
        uv = '紫外线强度指数（0-15）:\t\t%s' % (dataft['uv_index'].encode('utf-8'))
        self.msg = [city, date, weather, tmp, hum, wind, vis, pcpn, uv]


class air_weather(Weather):
    def __init__(self, url, city, key):
        super(air_weatherr, self).__init__(url, city, key)

    def get_weathermsg(self, station):
        for i in range(0,
                       len(self.w_json['HeWeather6'][0]['air_now_station'])):
            dataair = self.w_json['HeWeather6'][0]['air_now_station'][i]
            if str(dataair['air_sta'].encode('utf-8')) == str(station):
                break
        # 解析json格式化输出当前天气信息
        aqi = '空气质量指数：\t%s' % (dataair['aqi'].encode('utf-8'))
        qlty = '空气质量:\t%s' % (dataair['qlty'].encode('utf-8'))
        main = '主要污染物:\t%s' % (dataair['main'].encode('utf-8'))
        self.msg = [aqi, qlty, main]





class News(object):
    def __init__(self):
        self.news = 'a'
    def get_news(self):
        nwesurl = 'http://news.baidu.com/'
        res = urllib2.urlopen('http://news.baidu.com/').read()
        soup = BeautifulSoup(res, 'lxml')
        links = soup.find_all('div', id="left-col-wrapper")
        res_list = links[0].find_all('a', target="_blank")
        news_list = []
        for i in range(0, len(res_list)):
            news_list.append(res_list[i].get_text())
            news_list.append(res_list[i].get('href'))
        for i in news_list:
            self.news = self.news + i + '\n'
        
    def passerror(self):
        if self.news != 'a':
            pass
        else:
            try:
                try:
                    return newmain()
                except:
                    try:
                        return newmain()
                    except:
                        try:
                            return newmain()
                        except:
                            try:
                                return newmain()
                            except:
                                try:
                                    return newmain()
                                except:
                                    return newmain()
            except:
                self.news = '   '          


def main():
    # 在和风天气注册后获得的key
    key = '0ebf0677d6d84db99b8091660a4b7278'
    # 实况天气
    # wtnow = 'https://free-api.heweather.com/s6/weather/now?'
    # 未来3天天气
    ftweather = 'https://free-api.heweather.com/s6/weather/forecast?'
    # 空气质量实况
    air_now = 'https://free-api.heweather.com/s6/air/now?'
    # 生活指数
    # life = 'https://free-api.heweather.com/s6/weather/lifestyle?'
    # 空气检测站点
    station = '长清党校'
    # 城市信息，此处为济南
    city = 'CN101120101'

    nw = Weather(ftweather, city, key)
    nw.get_weathermsg()
    nwmsg = nw.msg
    na = air_weather(air_now, city, key)
    na.get_weathermsg(station)
    namasg = na.msg
    txt = nwmsg[0] + '\n' + nwmsg[1] + '\n' + nwmsg[2] + '\n' + nwmsg[3] + '\n' + namasg[1] + '\n' + \
    nwmsg[5] + '\n' + nwmsg[8] + '\n' + nwmsg[4] + '\n' + namasg[0] + '\n' + namasg[2] + '\n' + \
    nwmsg[6] + '\n' + nwmsg[7]
    n = News()
    n.get_news()
    n.passerror()
    txt = txt + '\n' + n.news
    return txt