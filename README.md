## 此项目为基于树莓派4B，主要用于记录自己开发的各种坑及使用方法

先在这里写下几个常用的网址

| 镜像 | 软件 | 资料 |
| ----------------- | ---------------- | -------------- |
| [树莓派官方下载地址](https://www.raspberrypi.org/downloads/) | [树莓派boot文件项目地址](https://github.com/raspberrypi/firmware) | [树莓派实验室](https://shumeipai.nxez.com/) |
| [树莓派官方镜像站](https://downloads.raspberrypi.org/)       | [树莓派EEPROM项目地址](https://github.com/raspberrypi/rpi-eeprom) | [树莓派资源整理汇总](https://segmentfault.com/a/1190000021776077) |
| [清华镜像源](https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/) | [raspi-config](https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/) [安装脚本](./Scripts/00/official/raspi-config)|  [树莓派官方论坛](https://www.raspberrypi.org/forums/)       |
|           |           |        |


脚本下载命令

```bash
sudo apt-get install subversion
svn checkout https://github.com/Crazydear/Raspberry-4B/trunk/Scripts
```
# 项目列表

## 0. 树莓派基本介绍
## 1. 树莓派4B使用USB设备启动
## 2. 非官方系统尝试
## 3.搭建CCAA的下载环境
## 4.根据CUP温度控制风扇
## 5.定时语音播报
## 6.I2C 驱动 LCD1602 液晶屏.md

# 脚本列表

| 序号 | 脚本功能  | 链接     |
| ---- | ------------ | -------------- |
| 01   | 阿里云DDNS | [链接](./Scripts/00/aliddns) |
| 02   | Github文件下载  | [链接](./Scripts/00/Downgithub) |
| 03   | raspi-config安装脚本 | [链接](./Scripts/00/official/raspi-config) |
| 04   | vcgencmd安装脚本 | [链接](./Scripts/00/official/vcgencmd) |
| 14   | 风扇控制         | [Python版](./Scripts/00-09/04-fan.py)  \|  [shell版](./Scripts/00-09/04-fan.sh) |
| 15   | 定时播报 | [链接](./Scripts/00-09/05-broadcast.py) |
| 16   | LCD显示 | [链接](./Scripts/00-09/06-LCD1602.py)   |
| 17   | DHT11模块   | [链接](./Scripts/00-09/07-dht11a.py)  \|[链接2](./Scripts/00-09/07-dht11a.py)  |
| 18   | PCF8591模块 | [链接](./Scripts/00-09/08-PCF8591.py) |
| 19   | 网站状态检测  |  [链接](./Scripts/00-09/09-webstatus)  |
|       |           |

# 项目时间线

## 2020.07.10 入手树莓派

同时也购买了一些其他的零件，包括外壳，温湿度传感器

## Donate

如果你觉得此项目对你有帮助，可以捐助我，以鼓励项目能持续发展，更加完善

|    Alipay 支付宝      |  Wechat 微信     |
| -----------------     | ---------------- |
|![alipay](images/alipay_donate.jpg)|![wechat](images/WeChat_donate.jpg)|
