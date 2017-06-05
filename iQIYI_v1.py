#-*-coding=utf-8-*-
__author__ = 'rocky chen'
from uiautomator import device as d
import time
def testcase():
    time.sleep(2)
    d(text=u'下载').click()

testcase()