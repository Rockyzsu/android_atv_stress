#-*-coding=utf-8-*-
__author__ = 'xda'
from uiautomator import device as d
import time
def ScreenOnOff(count):
    d.screen.on()
    time.sleep(3)
    d.press.home()
    d.press.down()
    d.press.down()
    d.press.down()
    d.press.down()
    d.press.down()
    d.press.right()
    d.press.right()
    d.press.right()
    d.press.right()
    d.press.right()
    d.press.right()
    d.press.right()
    if d(text='Power').exists == False:
        print "Failed"
        d.screenshot('snapshot_%d.png' %count)
    d.press.enter()
    time.sleep(3)
    d.press.right()
    d.press.enter()

    time.sleep(12)
    print "cycles %d" %count

def main():
    for i in range(500):
        ScreenOnOff(i)

main()
