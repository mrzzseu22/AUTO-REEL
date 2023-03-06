import sys
import openpyxl
import os.path
import shutil
import os
import subprocess
import re
import xlsxwriter
import pyotp
from appium import webdriver
import configuration
import pandas as pd
from multiprocessing import Process
from PyQt5.QtWidgets import *
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSettings
from PyQt5 import uic
from datetime import datetime
from auto_adb import AutoADB

class Driver:
	def __init__(self, devices, sys_port):
		self.devices = devices
		self.sys_port = int(sys_port)

		os.popen("adb -P 5037 -s {0} forward --remove tcp:{1}".format(self.devices, self.sys_port))

		self.caps = {
	      'platformName': "Android",
	      'udid': self.devices,
	      'skipLogcatCapture': True,
	      'appPackage': "com.facebook.katanc",
	      'appActivity': "com.facebook.katana.LoginActivity",
	      'automationName': 'UiAutomator2',
	      'autoGrantPermissions': True,
	      'unicodeKeyboard': True,
	      'resetKeyboard': True,
	      'autoLaunch': False,
	      'disableAndroidWatchers': True,
	      'disableWindowAnimation': True,
	      'printPageSourceOnFindFailure': False,
	      'gpsEnabled': False,
	      'systemPort': self.sys_port,
	      'newCommandTimeout': 99999,
	      'noReset': True,
	      'fullReset': False,
	      'debug': False,
	      'log_level': "info"
	    }

		self.url = 'http://127.0.0.1:4723/wd/hub'
		self.driver = webdriver.Remote(self.url, self.caps)
		

	def start_driver(self):

		return self.driver


