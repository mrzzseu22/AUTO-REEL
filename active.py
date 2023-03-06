import re
import schedule
from PyQt5 import QtCore, QtGui, QtWidgets
from appium import webdriver
import os
import time
import threading
import string
import random
import base64
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from appium.webdriver.common.touch_action import TouchAction
import names
import unittest
import json
import requests
import cv2
from pyotp import *
from selenium import webdriver
import subprocess
import schedule
from appium import webdriver
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from appium.webdriver.common.touch_action import TouchAction
from pyotp import *
from auto_adb import AutoADB
from class_driver import Driver
import configuration
from like_post import *

auto = AutoADB()
device_list  = auto.getDevices()
print(device_list)

def runtest(l):
	port = 8200 + l
	devices = device_list[l]
	dri = Driver(devices, port)
	driver = dri.start_driver()
	time.sleep(5)

	fake_gps(driver, auto, devices)
	time.sleep(3)

	packages = ['com.facebook.katana']


	for pack in packages:
		
		# rotate_hma(driver, auto, devices)
		# time.sleep(3)

		# clear_recent_app(auto, devices)
		# time.sleep(1)

		auto.openPackage(devices, pack)
		time.sleep(10)

		callout = [lambda: read_notification(driver, auto, devices, 3, 2, 1, pack),
             lambda: add_friend(driver, auto, devices, 2, 3, pack),
             lambda: accept_friend(driver, auto, devices, 5, 4, pack),
             lambda: scroll_newfeed(driver, auto, devices, 1, 2, 0, "Wow", 120, 4, pack),
             lambda: scroll_newfeed(driver, auto, devices, 0, 0, 0, "Wow", 120, 30, pack),
             lambda: scroll_reel(driver, auto, devices, react = 2, timeout = 240, delay_watch = 10, package = pack)
             #lambda: change_info_action(driver, auto, devices),
             #lambda: view_storie(driver, auto, devices, 120)
             ]

		
		random.shuffle(callout)
		for i in callout:
			time.sleep(3)
			i()

		time.sleep(5)
		auto.stopPackage(devices, pack)
		time.sleep(3)

		clear_recent_app(auto, devices)
		time.sleep(3)

	auto.keyevent(devices, "3")


		

	
	


  # driver.quit()



threads = []

for l in range(len(device_list)):
    threads += [threading.Thread(target=runtest,args={l},)]
for t in threads:
    t.start()
for t in threads:
    t.join()