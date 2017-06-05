#-*-coding=utf-8-*-
__author__ = 'rocky chen'
'''
Test iQIYI MediaCenter
Copy media content into usb drive and insert into device
'''
from uiautomator import device as d
import subprocess,time,re

class MediaCenter_Test():
    def __init__(self):
        self.package='com.tvos.EnjoyCenter'
        self.activity='com.tvos.EnjoyCenter/.media.VideoActivity'
        self.enjoy='com.tvos.EnjoyCenter/.app.MainActivity'


    def run_cmd(self,cmd):
        try:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            return p.stdout.read()

        except Exception,e:
            print e
            return None

    def launch(self):
        self.run_cmd('adb root')
        time.sleep(3)

        #stop_cmd='adb shell am force-stop %s' %self.package
        launch_cmd = 'adb shell am start -n %s' %self.enjoy
        #self.run_cmd(stop_cmd)

        self.run_cmd(launch_cmd)
        time.sleep(3)
        d.press.enter()
        for i in range(30):
            d.press.down()
            time.sleep(2)
        d.press.enter()
        time.sleep(5)
        d.press.enter()

        for _ in range(20):
            d.press.right()
            time.sleep(2)
            d.press.enter()
            time.sleep(2)
            d.press.enter()
            d.press.left()
            d.press.left()
            d.press.enter()
            time.sleep(2)
            d.press.enter()
            d.press.enter()
            d.press.enter()
            d.press.enter()
            time.sleep(2)

    def kill_app(self,package):
        self.run_cmd('adb root')
        time.sleep(3)
        s=self.run_cmd('adb shell ps')
        p='.*?\s+(\d+)\s+\d+\s+\d+\s+\d+ SyS_epoll_ .*? S %s' %package
        result=re.findall(p,s)
        t=result[0]
        cmd='adb shell kill %s' %t
        s1=self.run_cmd(cmd)
        d.press.back()
        time.sleep(3)

    def testcase(self):
        self.launch()
        self.kill_app(self.package)


obj=MediaCenter_Test()
obj.testcase()
#obj.kill_app('com.tvos.EnjoyCenter')