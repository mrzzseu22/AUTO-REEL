import subprocess
import cv2
import numpy as np
import time
import pyotp
import threading
import os
import random
#from pyzbar.pyzbar import decode
from PIL import Image
import configuration
import re

class AutoADB():
    
    def __init__(self):
        self.config = configuration.Configure()

    def ExecuteCMD(self, cmd):

        output = subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        # print(output)

#        output = subprocess.check_output(cmd)
#        if "Warning" in output.decode('utf-8'):
#            output = subprocess.check_output(cmd)
#            time.sleep(5)
#            if "Warning" in output.decode('utf-8'):
#                output = subprocess.check_output(cmd)
#                time.sleep(5)

        return output
    def ExecuteCMD_output(self, cmd):
        output = subprocess.check_output(cmd).decode('utf-8')

        return output

    def getDevices(self):
        listdevice = []
        devices = str(subprocess.check_output("adb devices", shell=True)).replace("b'List of devices attached\\r\\n", '').replace("'", '').replace('bList of devices attached ', '').split('\\r\\n')
        for device in devices:
            if device != '':
                listdevice.append(device.split('\\tdevice')[0])
        return listdevice

    def check_uid_backup(self, path):
        check_uid = os.path.exists(path)
        return check_uid

    def tap(self, deviceID, x, y):
        return self.ExecuteCMD((self.config.TAP_DEVICES).format(deviceID,x,y))

    def key(self, deviceID, key):
        return self.ExecuteCMD((self.config.KEY_DEVICES).format(deviceID, key))

    def inputText(self, deviceID, paste, text, delay):

        if paste == 0:

            for i in text:
                self.ExecuteCMD((self.config.INPUT_TEXT_DEVICES).format(deviceID,i))
                time.sleep(delay)

        else:
            self.ExecuteCMD((self.config.INPUT_TEXT_DEVICES).format(deviceID,text))

    def clearpackage(self, deviceID, package):
        return self.ExecuteCMD((self.config.CLEAR_PACKAGE).format(deviceID,package))

    def swipe(self, deviceID, x1, y1, x2, y2, ms):
        return self.ExecuteCMD((self.config.SWIPE_DEVICES).format(deviceID, x1, y1, x2, y2, ms))

    def install(self, deviceID, apk):
        return self.ExecuteCMD((self.config.INSTALL_APP).format(deviceID,apk))

    def uninstall(self, deviceID, apk):
        return self.ExecuteCMD((self.config.UNINSTALL_APP).format(deviceID,apk))

    def push(self, deviceID, file, location):
        return self.ExecuteCMD((self.config.PUSH_FILE_FROM_DEVICES).format(deviceID, file, location))

    def push_pic(self, deviceID, pf_path):
        count_pic = len([pf for pf in os.scandir(pf_path)])
        print(count_pic)
        ran_pic = random.randint(1, count_pic)
        print(ran_pic)
        pic_name = "\\pf({0}).jpg".format(str(ran_pic))

#        self.ExecuteCMD((self.config.REMOVE_FILEFROM_DEVICES).format(deviceID, "/sdcard/Pictures/*"))
        self.ExecuteCMD((self.config.PUSH_FILE_FROM_DEVICES).format(deviceID, pf_path+pic_name, "/sdcard/Pictures/pf.jpg"))
        time.sleep(0.1)
        self.ExecuteCMD((self.config.SCAN_PIC).format(deviceID, "sdcard/Pictures/pf.jpg"))



    def pull(self, deviceID, file, location):
        return self.ExecuteCMD((self.config.PULL_FILE_FROM_DEVICES).format(deviceID,file, location))

    def keyevent(self, deviceID, key):
        return self.ExecuteCMD((self.config.KEY_DEVICES).format(deviceID,key))

    def screenShoot(self, deviceID):

        file = ("/sdcard/screen_{0}.png").format(deviceID)
        self.ExecuteCMD((self.config.CAPTURE_SCREEN_TO_DEVICES).format(deviceID))
        self.Pull(deviceID,file,"")

    def findImage(self, deviceID, image):

        self.ScreenShoot(deviceID)
        img = cv2.imread(image)

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("screen_{0}.png".format(deviceID), 0)

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        THRESHOLD = 0.9
        loc = np.where(res >= THRESHOLD)

        for y, x in zip(loc[0], loc[1]):
            if x or y:
                return True
        return False

    def clickImage(self, deviceID, image):

        self.ScreenShoot(deviceID)
        img = cv2.imread(image)

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        template = cv2.imread("screen_{0}.png".format(deviceID), 0)

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        THRESHOLD = 0.9
        loc = np.where(res >= THRESHOLD)

        for y, x in zip(loc[0], loc[1]):
            return self.Tap(deviceID, x+6, y+6)

    def get2FA(self, code_2fa):
        to_otp =pyotp.TOTP(code_2fa)
        return to_otp.now()

    def set_brightness(self, deviceID, level):
        self.ExecuteCMD((self.config.OFF_AUTO_BRIGHNESS).format(deviceID))
        self.ExecuteCMD((self.config.SET_BRIGHNESS).format(deviceID, level))

    def disable_rotate(self, deviceID):
        return self.ExecuteCMD((self.config.DISABLE_ROTATE).format(deviceID))

    def on_Off_screen(self, deviceID):
        return self.ExecuteCMD((self.config.ON_OFF_SCREEN).format(deviceID))

    def reboot(self, deviceID):
        return self.ExecuteCMD((self.config.REBOOT).format(deviceID))

    def shut_down(self, deviceID):
        return self.ExecuteCMD((self.config.SHUTDOWN).format(deviceID))

    def get_device_name(self, deviceID):
        return self.ExecuteCMD_output((self.config.GET_DEVICES_NAME).format(deviceID))


    def enablewifi(self, deviceID):
        return self.ExecuteCMD("adb -s {0} shell su -c 'svc wifi enable'".format(deviceID))

    def disablewifi(self, deviceID):
        return self.ExecuteCMD("adb -s {0} shell su -c 'svc wifi disable'".format(deviceID))

    def airplaneon(self, deviceID):
        self.ExecuteCMD((self.config.AIRPLANE_ON).format(deviceID))
        self.ExecuteCMD((self.config.AIRPLANE_MODE).format(deviceID))

    def off_volume(self, deviceID, level):
        self.ExecuteCMD((self.config.SET_VOLUME).format(deviceID, level))

    def airplaneoff(self, deviceID):
        self.ExecuteCMD((self.config.AIRPLANE_OFF).format(deviceID))
        self.ExecuteCMD((self.config.AIRPLANE_MODE).format(deviceID))

    def grant(self, deviceID, package, permission):
        return self.ExecuteCMD((self.config.GRANT).format(deviceID, package, permission))

    def openPackage(self, deviceID ,package):
        return self.ExecuteCMD((self.config.OPEN_PACKAGE).format(deviceID, package))

    def stopPackage(self, deviceID ,package):
        return self.ExecuteCMD((self.config.FORCE_STOP).format(deviceID, package))

    def opendeeplink(self, deviceID, deep_link, package):
        return self.ExecuteCMD((self.config.OPEN_DEEPLINK).format(deviceID, deep_link, package))

    def clearcache(self, deviceID, package):
        return self.ExecuteCMD((self.config.CLEAR_CACHE).format(deviceID, package))

    def resolution(self, deviceID, wh):
        resolution_result = self.ExecuteCMD_output((self.config.GET_SCREEN_RESOLUTION).format(deviceID))
        resolution_h_w = resolution_result.replace("Physical size: ", "").replace("\r\n", "").split("x")

        if wh == "x":
            w = int(resolution_h_w[0])
            return w

        elif wh == "y":
            h = int(resolution_h_w[1])
            return h

        elif wh == "x_y":
            w, h = int(resolution_h_w)
            return w, h

        else:
            print("wrong paramater")

    def mirror(self, deviceID, off_screen, size, x, y):
        if off_screen == 1:
            self.ExecuteCMD((self.config.MIRROIR_OFF_SCREEN).format(deviceID, size, x, y))

        else:
            self.ExecuteCMD((self.config.MIRROIR).format(deviceID, size, x, y))




    def mirror_multi(self, list_devices, off_screen, size, amount_devices, amount_on_y):
        x = 0
        y = 30

        screen_x = 1080
        screen_y = 1920 / amount_on_y

        if len(list_devices) <= amount_devices:
            device_index = len(list_devices)

        elif amount_devices > len(list_devices):
            device_index = len(list_devices)

        else:
            device_index = amount_devices


        def runtest(x, index):
            device_mirror = list_devices[index]

            if off_screen == 1:
                self.ExecuteCMD((self.config.MIRROIR_OFF_SCREEN).format(device_mirror, size, x, y))

            else:
                self.ExecuteCMD((self.config.MIRROIR).format(device_mirror, size, x, y))

            

        for index in range(device_index):
            th = threading.Thread(target=runtest, args=[x, index])
            th.start()
            index += 1

            x += int(screen_y)
            if index == amount_on_y:
                y += 530
                x = 0

            elif index == amount_on_y*2:
                y = 30
                x = 0

            elif index == amount_on_y*3:
                y += 530
                x = 0

            elif index == amount_on_y*4:
                y = 30
                x = 0

            elif index == amount_on_y*5:
                y += 530
                x = 0

            elif index == amount_on_y*6:
                y = 30
                x = 0

            time.sleep(0.2)


    

#k = auto.check_uid_backup(r"C:\Users\MrZz Seu\Desktop\New Swap\Backup\100086494927796")
#print(k)

# auto = AutoADB()
# devices = auto.getDevices()[0]
# x = auto.resolution(devices, "x")
# y = auto.resolution(devices, "y")
# auto.tap(devices, str(x/2), str(y/2))
# time.sleep(0.2)
# auto.tap(devices, str(x/2), str(y/2))
# 
# print(devices)
#auto.push_pic(devices, "pf")
#print(devices)
#auto.resolution(devices, "x")

#print(x)


#auto.mirror(devices, 0, "500", "0", "30")
#devices = auto.getDevices()[0][1]

#def sss()
#    kk = auto.mirror(devices, 0, "500", "270", "30")
#kk()
#auto.mirror_multi(auto.getDevices()[0], 0, "350", 10, 9)
#print(type(devices))

#random_swipe = ["150", "200", "250", "300", "310"]

#for i in range(50):

#    auto.swipe(devices, "360", "1000", "360", "400", random.choice(random_swipe))
#    auto.swipe(devices, "360", "805", "360", "800", "0")
#    time.sleep(random.uniform(0.5, 7))

