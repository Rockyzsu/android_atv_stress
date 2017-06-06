#-*-coding=utf-8-*-
__author__ = 'rocky chen'
#connect kb or ts firstly
from uiautomator import device as d
import time,subprocess
def skip_setup_case():
    d.wait()
    time.sleep(30)
    d.press.enter()
    time.sleep(2)
    for _ in range(25):
        d.press.down()
        time.sleep(1)

    d.press.enter()
    time.sleep(2)
    d.press.back()
    cmd='adb shell input text 5G'
    subprocess.Popen(cmd, shell=True)
    d.press.enter()
    time.sleep(2)
    d.press.down()
    d.press.down()
    d.press.back()
    cmd='adb shell input text asdfqwer'
    subprocess.Popen(cmd, shell=True)
    time.sleep(15)
    d.press.enter()
    time.sleep(2)
    d.press.back()
    cmd='adb shell input text xxxxxxx'
    d.press.enter()
    time.sleep(5)
    cmd='adb shell input text xxxxxx'
    subprocess.Popen(cmd, shell=True)
    time.sleep(5)
    d.press.enter()
    d.press.enter()




skip_setup_case()
