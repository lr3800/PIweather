# -*- coding: utf-8 -*-
#BY:LR3800
import sys,urllib2, json,os,datetime

reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8') #这个是解决合成中文文本的时候，Unicode和utf-8编码问题的，可以尝试注释掉会不会报错

#调用和风天气的API
url = 'https://free-api.heweather.com/v5/weather?city=guangzhou&key=你的KEY'
req = urllib2.Request(url)
resp = urllib2.urlopen(req).read()

#将JSON转化为Python的数据结构
json_data = json.loads(resp)
data = json_data['HeWeather5'][0]

#获取PM2.5的值
pm25 = data['aqi']['city']['pm25']
#获取空气质量
air_quality = data['aqi']['city']['qlty']

#获取城市
city = data['basic']['city']

#获取现在的天气、温度、体感温度、风向、风力等级
now_weather = data['now']['cond']['txt']
now_tmp = data['now']['tmp']
now_fl = data['now']['fl']
now_wind_dir = data['now']['wind']['dir']
now_wind_sc = data['now']['wind']['sc']

#今天的天气
today = data['daily_forecast'][0]
weather_day = today['cond']['txt_d']
weather_night = today['cond']['txt_n']
tmp_high = today['tmp']['max']
tmp_low = today['tmp']['min']
wind_dir = today['wind']['dir']
wind_sc = today['wind']['sc']

#天气建议

#舒适度
comf = data['suggestion']['comf']['brf']
comf_txt = data['suggestion']['comf']['txt']

#流感指数
flu = data['suggestion']['flu']['brf']
flu_txt = data['suggestion']['flu']['txt']

#穿衣指数
trav = data['suggestion']['trav']['brf']
trav_txt = data['suggestion']['trav']['txt']


now = datetime.datetime.now()

data = now.strftime('%Y-%m-%d %H:%M:%S')
weather_forcast_txt = "当前时间%s,%s今天白天天气:%s,夜间天气:%s,最高气温:%s摄氏度,最低气温:%s摄氏度, 今天外出：%s,%s 当前天气：%s,当前温度:%s摄氏度,当前风力:%s,PM2.5值%s,空气质量：%s"%(data,city,weather_day,weather_night,tmp_high,tmp_low,trav,trav_txt,now_weather,now_tmp,now_wind_sc,pm25,air_quality)

print weather_forcast_txt

#语言播报
url = "http://tsn.baidu.com/text2audio?tex=" + weather_forcast_txt + "&lan=zh&per=3&spd=5&cuid=pi&ctp=1&tok=你的百度语音合成tok"
os.system('mpg123 "%s"'%(url))





