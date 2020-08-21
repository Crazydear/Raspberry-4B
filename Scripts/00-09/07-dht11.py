#!/usr/bin/python3
#encoding:utf-8

import Adafruit_DHT

def get_data():
    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 25

    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}°C | Humidity={1:0.1f}%".format(temperature, humidity))
        with open('/var/www/html/pi-dashboard/temp.txt','w') as f:
            f.write("温度:{0:0.1f}°C | 湿度:{1:0.1f}%".format(temperature, humidity))
    else:
        print("获取传感器数据失败，请检查")

if __name__ == '__main__':
    get_data()
