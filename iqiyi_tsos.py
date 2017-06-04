# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
from uiautomator import device as d
import time, subprocess, os, datetime, re


class IQIYI_Stress():
    def __init__(self):

        # path=os.path.join(os.getcwd(),)
        self.date = datetime.datetime.now().strftime('%H-%M-%S')
        self.logname = "Logcat_%s.log" % self.date
        #windows not working
        #self.getLog()

    # 进入本地管理
    def localManagement(self):
        d.press.home()
        #on recommandation bar
        time.sleep(2)
        d.press.down()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.right()
        time.sleep(1)
        d.press.enter()
        time.sleep(2)

    def checkQuene(self):
        #self.localManagement()
        print "B"
        if d(text=u'游戏').exists:
            print "B"
            i1 = d(text=u'游戏').info
            time.sleep(2)
            d(text=u'游戏').click()
            i2 = d(text=u'游戏').info
            for (k, v) in i1.items():
                print '(%s : %s)' % (k, v)

            print "*" * 10

            for (k, v) in i2.items():
                print '(%s : %s)' % (k, v)
        if d(text=u'最近安装').exists:
            print 'find game'
    def getLog(self):
        if self.execute_cmd('adb wait-for-device') == 0:
            print "device not connect to Host"
            exit()
        #windows 放不了后台
        cmd = 'adb logcat -v time >%s &' % self.logname
        os.system(cmd)

    def execute_cmd(self, cmd):
        try:
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            p.communicate()
            p.wait()
            return 1

        except Exception, e:
            print e
            return 0

    def testcase(self):
        print "debug"

        d.press.back()
        d(text=u"游戏").click()
        d(text=u"游戏").click()

        if d(textContains=u'狂野飙车').exists:
            print "Got version"
            print d(textContains=u'狂野飙车').info
        else:
            print "Can't get version"


        '''
        if d(text=u'剩余').exists:
            print "open"
            print d(text=u'剩余').info
        else:
            print "Can't open"
        '''
        #self.search_game('test')

        #self.input_name()
        #self.download()
        #self.checkQuene()
        #self.delete_game()
        #self.getPackageName()
        #elf.delete_game_cmd('')
        #elf.getPackageName()
        #self.person_center()
        #self.check_login()
        #self.check_download('')

    def input_name(self):
        #从软键盘弹出来开始
        for _ in range(6):
            d.press.right()
            time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.enter()

        d.press.up()
        time.sleep(1)
        d.press.left()
        time.sleep(1)
        d.press.left()
        time.sleep(1)
        d.press.enter()

        time.sleep(2)
        d.press.down()
        time.sleep(1)
        d.press.right()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.enter()

        time.sleep(1)

        d.press.left()
        time.sleep(1)
        d.press.left()
        time.sleep(1)
        d.press.left()
        time.sleep(1)

        d.press.enter()

        time.sleep(1)

        d.press.up()
        time.sleep(1)
        d.press.up()
        time.sleep(1)
        d.press.up()
        time.sleep(1)
        d.press.left()
        time.sleep(1)
        d.press.left()
        time.sleep(1)
        d.press.left()
        time.sleep(1)
        d.press.left()
        time.sleep(1)
        d.press.enter()

        if d(text=u'狂野飙车').exists:
            print "Search result passed"
            print d(text=u'狂野飙车').info
        else:
            print "Can't find game "

        d.press.back()
        time.sleep(1)

        d.press.enter()
        time.sleep(3)
        print "start to download"


    def wifi_connect(self):
        print "WIFI connect"
        ap='lenovo'
        passwd='xxx'
        def_timeout=120
        d.press.home()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.down()
        d.press.down()
        time.sleep(1)
        d.press.right()
        time.sleep(1)
        d.press.right()

        d.press.enter()
        time.sleep(3)
        d.press.enter()
        time.sleep(3)
        d.press.down()
        d.press.down()
        d.press.down()
        d.press.down()
        d.press.down()

        d.press.enter()
        time.sleep(2)
        cmd = 'adb shell input text %s' % ap
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        cmd = 'adb shell input keyevent KEYCODE_ESCAPE'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(1)
        d.press.enter()
        time.sleep(1)

        d.press.down()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.enter()
        cmd = 'adb shell input text %s' % passwd
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

        cmd = 'adb shell input keyevent KEYCODE_ESCAPE'
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        time.sleep(1)
        d.press.enter()
        time.sleep(1)
        if d(text=u"连接成功").wait.exists(timeout=def_timeout * 1000) == False:
            print "connecting time over time"
            print "Fail to connect AP"
            return 1
        d(text=u"连接成功").wait.exists(timeout=200000)
        return 0

    def search_game(self, name='kybc'):
        d.press.home()
        time.sleep(2)
        d.press.down()
        time.sleep(2)
        d.press.right()
        time.sleep(1)
        d.press.enter()
        time.sleep(3)
        d.press.up()
        time.sleep(3)
        d.press.up()
        time.sleep(1)
        d.press.enter()
        time.sleep(3)
        d.press.right()
        time.sleep(1)

        #self.execute_cmd('adb shell input text 狂野飙车')
        #this not work
        #self.execute_cmd('adb shell input text kybc')


    def download(self):
        d.press.enter()
        time.sleep(5)

    def check_download(self,gamename):
        self.localManagement()
        d(text=u'队列').click()

        time.sleep(3)

        while 1:
            if d(text=gamename).exists:
                time.sleep(30)
            else:
                d.press.back()
                time.sleep(2)

                d(text=u'游戏').click()
                time.sleep(1)
                print u"下载完毕"
                break




    def getAppID(self):
        #在下载的时候才能获取到
        p = 'getGameStatus appId:(\d+)'
        fp = open(self.logname, 'r').read()
        s = re.findall(p, fp)
        print s[0]

    def delete_game_UI(self):
        self.localManagement()
        d(text=u'游戏').click()
        if d(textContains=u'1.53GB').exists:
            d.press.enter()
            time.sleep(3)
            try:
                d(text=u'卸载游戏').click()
                time.sleep(2)
                d.press.enter()
                #查看包名有没有这个

            except Exception,e :
                print e
                return False

    def delete_game_cmd(self,package):
        packagename='com.baxa.mappytv'
        cmd='adb shell pm uninstall %s' %packagename
        self.execute_cmd(cmd)


    def getPackageName(self):
        p = subprocess.Popen('adb shell pm list packages', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        #p.communicate()
        #p.wait()
        package_list=p.stdout.read()
        #package_list
        #pattern='package:com.gameloft.android.HEP.GloftA8HP'
        pattern='package:com.baxa.mappytv'
        result=re.findall(pattern,package_list)
        if len(result)==0:
            print "game has been deleted"
            return 1
        else:
            print "Game doesn't uninstall"
            return 0

    def check_login(self):
        if d(text=u'已购游戏').exists:
            print "已登录爱奇艺账户"
            return 1
        else:
            print "未登录爱奇艺账户"
            return 0

    def person_center(self):
        d.press.home()
        #on recommandation bar
        time.sleep(2)
        d.press.down()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.down()
        time.sleep(1)
        d.press.enter()
        time.sleep(2)

    def tvos_12723(self):
        #点击"卸载游戏"后的弹窗(V1.7)
        self.delete_game_UI()
        self.person_center()
        self.check_login()
        self.search_game()
        self.input_name()





def main():

    obj = IQIYI_Stress()
    obj.testcase()
    #狂野飙车的 包名 com.gameloft.android.HEP.GloftA8HP

if __name__ == '__main__':
    main()