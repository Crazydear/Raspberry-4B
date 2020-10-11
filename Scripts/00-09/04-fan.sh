#!/bin/bash
# 利用crontab定时，每隔一分钟运行一次

if [ -e /sys/class/gpio/gpio26/direction ]
then
echo "已经挂载"
else
echo "未挂载"
echo 26 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio26/direction

fi

tem=$(cat /sys/class/thermal/thermal_zone0/temp)
echo $tem

if [ $tem -ge 65000 ]
then
echo out > /sys/class/gpio/gpio26/direction
echo 0 > /sys/class/gpio/gpio26/value
fi

if [ $tem -le 40000 ]
then
echo 1 > /sys/class/gpio/gpio26/value 
echo "温度不高"
fi
