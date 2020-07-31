#!/usr/bin python3
# -*- coding:utf-8 -*-
# Author:李绍丰

# ****************************************************************
# 程序功能：风扇控制
# 模块划分：开启风扇，关闭风扇，获取CPU温度
# ****************************************************************

import RPi.GPIO as GPIO
import time

fan_pin = 14
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_pin,GPIO.OUT)

def on_fan():
    GPIO.output(fan_pin,False)

def off_fan():
    GPIO.output(fan_pin,True)

def get_CPU_temp():
    with open(r"/sys/class/thermal/thermal_zone0/temp") as file:
        temp = float(file.read()) / 1000
    return temp

# on_fan()
off_fan()
while True:
    temp = get_CPU_temp()
    if temp > 55:
        on_fan()
    if temp < 38:
        off_fan()
    time.sleep(60)
