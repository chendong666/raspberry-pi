# -*-coding:utf-8-*-
# python版本 2.7

import json
import urllib
import urllib2
import datetime
from bs4 import BeautifulSoup

# 编码网址信息
def urlencode(url, key, city):
    massage = {}
    # 在和风天气注册后获得的key
    massage['key'] = key
    massage['location'] = city
    urldata = urllib.urlencode(massage)
    encodeurl = url + urldata
    return encodeurl


# 获取当前天气信息json
def get_json(url):
    html = urllib2.urlopen(url).read()
    return json.loads(html)


# 解析json格式化输出当前天气信息
def outputdata(databasic, dataft, dataair):
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
    aqi = '空气质量指数：\t%s' % (dataair['aqi'].encode('utf-8'))
    qlty = '空气质量:\t%s' % (dataair['qlty'].encode('utf-8'))
    main = '主要污染物:\t%s' % (dataair['main'].encode('utf-8'))
    txt = city + '\n' + date + '\n' + weather + '\n' + tmp + '\n' + qlty + \
          '\n' + wind + '\n' + uv + '\n' + hum + '\n' + aqi + '\n' + main + '\n' + \
          vis + '\n' + pcpn
    return txt


def weather(city,station):
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
    # 编码网址
    ftweather_e = urlencode(ftweather, key, city)
    air_now_e = urlencode(air_now, key, city)
    # 获取并初步解析json数据
    wjson = get_json(ftweather_e)
    basic = wjson['HeWeather6'][0]['basic']
    for i in [0,1,2]:
        ftwe = wjson['HeWeather6'][0]['daily_forecast'][i]
        if str(ftwe['date'].encode('utf-8')[-2:]) == str(datetime.datetime.now().day):
            break
    wjson = get_json(air_now_e)
    for i in range(0,len(wjson['HeWeather6'][0]['air_now_station'])):
        air = wjson['HeWeather6'][0]['air_now_station'][i]
        if str(air['air_sta'].encode('utf-8')) == str(station):
            break
    # 输出
    return outputdata(basic, ftwe, air)



# 解析新闻网页
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
        x = x + i + '\n'
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
