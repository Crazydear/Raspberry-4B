#!/user/bin/env python 
import smbus
import time
import sys
import LCD1602 as LCD
 
if __name__ == '__main__':  
    LCD.init_lcd()
    time.sleep(1)
    LCD.print_lcd(2, 0, 'WWW.QUWJ.COM')
    for x in xrange(1, 4):
        LCD.turn_light(0)
        LCD.print_lcd(4, 1, 'LIGHT OFF')
        time.sleep(0.5)
        LCD.turn_light(1)
        LCD.print_lcd(4, 1, 'LIGHT ON ')
        time.sleep(0.5)
 
    LCD.turn_light(0)
     
    while True:
        now = time.strftime('%m/%d %H:%M:%S', time.localtime(time.time()))
        LCD.print_lcd(1, 1, now)
        time.sleep(0.2)
