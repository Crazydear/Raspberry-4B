#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:李绍丰

# ****************************************************************
# 程序功能：定时播报
# 模块划分：获取农历日期，获取当前时间，获取天气，文字转语音，播放语音
# ****************************************************************

import requests
import time
import os
import Adafruit_DHT

def get_weather():
    url = "https://api.asilu.com/weather/?city=天津"
    response = requests.get(url).json()
    data = response['weather'][0]
    text = "{0},{1},{2}".format(data['weather'],data["temp"],data["wind"])
    return text


def get_date():
    data = time.strftime("%m月%d日", time.localtime())
    lunurl = "http://api.xlongwei.com/service/datetime/convert.json"
    response = requests.get(lunurl).json()
    text = "今天是{0}，{1}。".format(data,response['nongli'])
    return text


def get_time():
    times = time.strftime("%H时%M分", time.localtime())
    text = "现在是{0}。".format(times)
    return text


def get_temp():
    sensor = Adafruit_DHT.DHT11
    pin = 25 #GPIO25
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return "室内温度{0}℃，相对湿度{1}%".format(temperature,humidity)
    

def get_mp3(text=None):
    url = "http://tools.bugscaner.com/api/tts/"
    data = {'text': text,'yusu': 10,'fasheng': 0}
    session = requests.Session()
    reponse = session.post(url,data=data).json()
    reslut = session.get("http://tools.bugscaner.com/api/tts/?"+reponse["video"])
    with open("/home/pi/python/audio.mp3","wb") as f:
        f.write(reslut.content)
    print("Audio success")


def playAudio():
    os.system("mplayer /home/pi/python/audio.mp3")


# aa = get_weather()
bb = get_time()
te = get_temp()
get_mp3(bb+te)
playAudio()