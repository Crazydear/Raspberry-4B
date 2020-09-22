#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ------------------------------------------------------
#
#       您可以使用下面语句将此脚本导入另一个脚本：
#           “import PCF8591 as ADC”
#
#   ADC.Setup(Address)  # 查询PCF8591的地址：“sudo i2cdetect -y 1”
# i2cdetect  is  a  userspace  program to scan an I2C bus for devices.
# It outputs a table with the list of detected devices on the specified bus.
#   ADC.read(channal)   # Channal范围从0到3
#   ADC.write(Value)    # Value范围从0到255
#
# ------------------------------------------------------
# SMBus (System Management Bus,系统管理总线)
import smbus  # 在程序中导入“smbus”模块
import time

class PCF8591:
    def __init__(self,Addr):
        # for RPI version 1, use "bus = smbus.SMBus(1)"
        # 0 代表 /dev/i2c-0， 1 代表 /dev/i2c-1 ,具体看使用的树莓派那个I2C来决定
        self.bus = smbus.SMBus(1)  # 创建一个smbus实例
        # 在树莓派上查询PCF8591的地址：“sudo i2cdetect -y 1”
        self.address = Addr


    def read(self,chn):  # channel
        if chn == 0:
            self.bus.write_byte(self.address, 0x40)  # 发送一个控制字节到设备
        if chn == 1:
            self.bus.write_byte(self.address, 0x41)
        if chn == 2:
            self.bus.write_byte(self.address, 0x42)
        if chn == 3:
            self.bus.write_byte(self.address, 0x43)
        self.bus.read_byte(self.address)  # 从设备读取单个字节，而不指定设备寄存器。
        return self.bus.read_byte(self.address)  # 返回某通道输入的模拟值A/D转换后的数字值


    def write(self,val):
        temp = val  # 将字符串值移动到temp
        temp = int(temp)  # 将字符串改为整数类型
        # print temp to see on terminal else comment out
        self.bus.write_byte_data(self.address, 0x40, temp)
        # 写入字节数据，将数字值转化成模拟值从AOUT输出


if __name__ == "__main__":
    PCF8591 = PCF8591(0x48)  # 在树莓派终端上使用命令“sudo i2cdetect -y 1”，查询出PCF8591的地址为0x48
    # 下面这种格式是配合RaspContronller自定义的组件
    result1 = "<result1>{}</result1>".format(PCF8591.read(0))  # 电位计
    result2 = "<result2>{}</result2>".format((255 - PCF8591.read(1)) / 2.55)  # 光敏电阻
    result3 = "<result3>{}</result3>".format(143 - PCF8591.read(2))  # 热敏电阻
    result4 = "<result4>{}</result4>".format(PCF8591.read(3))  # 自定义
    print(result1)
    print(result2)
    print(result3)
    print(result4)

