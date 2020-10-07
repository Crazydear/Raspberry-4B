#!/usr/bin python3.8
# -*- coding:utf-8 -*-

# 所需要的第三方库
# pip3 install python3-rpi.gpio
# pip3 install dht11
# pip3 install sqlite3

import RPi.GPIO as GPIO
import dht11
import sqlite3
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 25
instance = dht11.DHT11(pin = 25)
result = instance.read()

def sql_init():
	# 创建数据库表
	con = sqlite3.connect('/root/program/data/dht11.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)	# 硬盘上创建连接
	cur = con.cursor()	# 获取cursor对象
	# 执行sql创建表
	sql = 'create table domitory(id INTEGER PRIMARY KEY  AUTOINCREMENT ,datetime timestamp ,temperature,humidity)'
	try:
	    cur.execute(sql)
	except Exception as e:
	    print(e,'创建表失败')
	finally:
	    cur.close()	# 关闭游标
	    con.close()	# 关闭连接
	    
def sqlwrite(result):
	con = sqlite3.connect('/root/program/data/dht11.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
	cur = con.cursor()		# 获取cursor对象
	# 执行sql创建表
	sql = 'insert into domitory(datetime,temperature,humidity) values(?,?,?)'
	try:
	    cur.execute(sql,(datetime.datetime.now().replace(microsecond=0),result.temperature, result.humidity))	#提交事务
	    con.commit()
	    #print('插入成功')
	except Exception as e:
	    print(e,'插入失败')
	    con.rollback()
	finally:
	    cur.close()	# 关闭游标
	    con.close()	# 关闭连接


if __name__ == '__main__':   
    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        with open('/var/www/html/pi-dashboard/temp.txt','w') as f:
                f.write("温度:{0:0.1f}°C | 湿度:{1:0.1f}%".format(result.temperature, result.humidity))
        sqlwrite(result)
    else:
        print("Error: %d" % result.error_code)
