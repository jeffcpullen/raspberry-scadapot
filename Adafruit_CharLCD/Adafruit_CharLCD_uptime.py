#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()

cmd1 = "cat /proc/loadavg | awk '{print $1,$2,$3}'"
cmd2 = "free -m | grep Mem | awk '{print \"Mem Free \"$4\"m\"}'"

lcd.begin(16, 1)


def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

while 1:
    load = run_cmd(cmd1)
    mem = run_cmd(cmd2)
    lcd.clear()
#    lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
#    lcd.message('IP %s' % (ipaddr))
    lcd.message('%s\n%s' % (load, mem))
    sleep(2)
