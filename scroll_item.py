#-*-coding=utf-8-*-
__author__ = 'xda'
from uiautomator import device as d
import time
def scroll_page():
    for _ in range(7):
        d.press.down()
        time.sleep(2)
    for _ in range(7):
        d.press.up()
        time.sleep(2)




for _ in range(60):
    scroll_page()