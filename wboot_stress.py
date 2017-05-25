# -*-coding=utf-8-*-
__author__ = 'xda'
import re
import os,sys
import subprocess
import time


def run_cmd(cmdline, bailout=None):
    print "Running cmd: %s" % (cmdline)
    handle = subprocess.Popen(cmdline, shell=True)
    if bailout:
        fin_time = time.time() + bailout
        while handle.poll() == None and fin_time >= time.time():
            time.sleep(1)
            if time.time() >= fin_time and handle.poll() == None:
                print "Bailout exceeded[%s sec], killing process..." % (str(bailout))
                if sys.platform == "win32":
                    os.popen('TASKKILL /PID ' + str(handle.pid) + ' /F /T')
                else:
                    os.popen('kill -9 ' + str(handle.pid))
                return 9
    else:
        handle.wait()
        return handle.returncode;


class adb_utils:
    def __init__(self):
        if self.conn_check():
            self.online = 1
            self.execute("svc power stayon true")
        else:
            self.online = 0

    def conn_check(self):
        ctr = 2
        while ctr:
            ctr -= 1
            handle = subprocess.Popen("adb devices",
                                      shell=True,
                                      bufsize=-1,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)
            for line in handle.stdout:
                if re.search("\sdevice\s", line):
                    return 1
            run_cmd("adb kill-server")
            run_cmd("adb start-server")
        return 0

    def warm_boot(self):
        run_cmd("adb reboot", bailout=120)
        time.sleep(5)

    def boot_check(self):
        run_cmd("adb wait-for-devices logcat -v time > boot.log &", 120)
        bailout = 180
        while (bailout > 0):
            if (not os.system("grep  \"Boot is finished\" boot.log")):
                return 1
            time.sleep(5)
            bailout -= 5
        return 0

    def execute(self, cmdline):
        cmdline = "adb shell " + cmdline
        run_cmd(cmdline)


def hsic_enum_test(cmdline):
    cmdline = "adb shell " + cmdline
    handle = subprocess.Popen(cmdline,
                              shell=True,
                              bufsize=-1,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    enum_err = 0
    for line in handle.stdout:
        if re.search("No such file or directory", line):
            enum_err = 1
            print line
    return not (enum_err)


def usage():
    print "Usage:"
    print "\tpython wboot_stress.py --iterate <no of iterations needed>"
    exit(0)


def parse_cmdline():
    args = []
    if len(os.sys.argv) < 3:
        usage()
    i = 1
    while i < len(os.sys.argv):
        if os.sys.argv[i] == "--iterate":
            i += 1
            args.append(int(os.sys.argv[i]))
        else:
            print "Illegal argument!"
            usage()
        i += 1
    return args


def main():
    target = parse_cmdline()[0]
    adb = adb_utils()

    if not adb.online:
        print "ADB connection failed!"
        exit(1)

    wboot_cycles = 0
    while wboot_cycles < target:
        print "Reboot no: %d" % (wboot_cycles)
        adb.warm_boot()
        if not adb.boot_check():
            print "Warm boot failed!"
            break
        if not hsic_enum_test("ls /dev/smdcsd /dev/smdctl /dev/smdipc /dev/smdloop /dev/smdrfs /dev/smdrouter"):
            print "HSIC enumeration failed!"
            break
        wboot_cycles += 1

    print "No of successful cycles: %d" % (wboot_cycles)


if __name__ == "__main__":
    main()
