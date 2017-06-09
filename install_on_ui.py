#-*-coding=utf-8-*-
__author__ = 'rocky chen'
from uiautomator import device as d
import time
class QuickInstall():
    def __init__(self):
        pass
    def install(self):
        #d.dump('iqiyi.xml')
        if d(textContains=u'下载').exists:
            print "get"
            #d.press.enter()
            d(textContains=u'下载').click()
            time.sleep(5)
            if d(textContains=u'打开').wait.exists(timeout=120000)==0:
                print "Install time out"
                d.press.back()
                exit()
            d.press.back()
            time.sleep(3)
        else:
            print "not get"
            d.press.back()
            time.sleep(5)
    def testcase(self):
        for _ in xrange(10):
            d.press.enter()
            time.sleep(5)
            self.install()
            d.press.right()




obj=QuickInstall()
obj.testcase()