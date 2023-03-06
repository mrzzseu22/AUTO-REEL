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
from pymailtm import MailTm
from pyotp import *
from auto_adb import AutoADB
from class_driver import Driver
import configuration




#addfri = ("adb -s ") + devices + (" shell am start -a android.intent.action.VIEW -d fb://profile/100076852710559/friends")
#addfri1 = os.popen(addfri)
#force_stop = ("adb -s ") + devices + (" shell am force-stop com.facebook.katana")
#force_stop1 = os.popen(force_stop)

#open_fb1 = ("adb -s ") + devices + (" shell monkey -p 'com.facebook.katana' -c android.intent.category.LAUNCHER 1")
#open_fb11 = os.popen(open_fb1)

#time.sleep(10)


#time.sleep(5)

def react_post(driver, auto, devices, react, delay):

  auto.swipe(devices, "360", "1000", "360", "880", "100")

  actions = TouchAction(driver)

  random_react = ['//*[@content-desc="Like"]', '//*[@content-desc="Love"]', '//*[@content-desc="Care"]', '//*[@content-desc="Haha"]', '//*[@content-desc="Wow"]']

  if react == 1:

    try:

      like = driver.find_element_by_xpath('//android.widget.Button[@content-desc="Like button. Double tap and hold to react."]')
      if like.is_displayed():
        actions.long_press(like)
        actions.perform()

        time.sleep(delay)

        react = driver.find_element_by_xpath(random.choice(random_react))
        if react.is_displayed():
          print("Reaction")
          react.click()

          return True

        else:
          print("No Reaction")


    except:
      print("Not found react")
      return False

  else:
    print("No reaction btn")


#react_post(driver, 1, 2)

def comment_post(driver, auto, devices, cmt, input_opt, delay, cmt_text, package):

  if cmt == 1:

    try:

      cmt_btn = driver.find_element_by_xpath(
        '//android.widget.Button[@text="Comment"]')
      if cmt_btn.is_displayed():
        cmt_btn.click()

        time.sleep(delay)

        try:

          write_cmt = driver.find_element_by_xpath(
            '//android.widget.EditText[@index="1" or @text="Write a comment…"]')
          if write_cmt.is_displayed():

            if input_opt == 0:

              auto.inputText(devices, 0, cmt_text, 0.1)

            else:

              write_cmt.send_keys(cmt_text)

            send_cmt = driver.find_element_by_xpath(
              '//android.view.ViewGroup[@content-desc="Send"]')

            if send_cmt.is_displayed():
              send_cmt.click()

            else:
              print("Not found send_cmt")

            time.sleep(1)

            auto.keyevent(devices, "4")

            return True

        except:
          print("Not found write_cmt")

    except:
      print("Not found cmt btn")
      return False

  else:
    print("Not cmt")


def scroll_newfeed(driver, auto, devices, feed_watch, react, cmt, cmt_text, timeout, delay_watch, package):

  if feed_watch == 1:
    auto.opendeeplink(devices, "", package)

  else:
    auto.opendeeplink(devices, "watch", package)

  time.sleep(3)

  random_swipe = ["310", "305", "300", "295"]
  random_ms =  ["200", "250", "300", "350", "400"]
  minute_count = 0
  react_count = 0
  comment_count = 0

  while True:

    if int(minute_count) >= timeout:
      print("break")
      break

    else:

      auto.swipe(devices, "360", "1000", "360", random.choice(random_swipe), random.choice(random_ms))
      pass

    minute = random.randint(delay_watch-1, delay_watch)
    time.sleep(minute)
    random_list = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    random_percent = random.choice(random_list)

    if react >= 1:

      if react_count < react:
        if random_percent == 1:
          print(random_percent)

          try:

            if react_post(driver, auto, devices, 1, 2.2) == True:
              react_count += 1
              time.sleep(1)

          except:
            pass

    if cmt >= 1:

      if comment_count < cmt:
        if random_percent == 1:

          try:

            if comment_post(driver, auto, devices, 1, 1, 1, cmt_text) == True:
              comment_count += 1
              time.sleep(0.5)

          except:
            pass

    minute_count += int(minute)

  auto.opendeeplink(devices, "", package)


def scroll_reel(driver, auto, devices, react, timeout, delay_watch, package):

  x = auto.resolution(devices, "x")
  y = auto.resolution(devices, "y")
  random_swipe = ["310", "305", "300", "295"]
  random_ms =  ["200", "250", "300", "350", "400"]
  minute_count = 0
  react_count = 0

  auto.opendeeplink(devices, "faceweb/f?href=http://www.facebook.com/reel/1344554099721345", package)

  time.sleep(5)

  while True:

    if int(minute_count) >= timeout:
      print("break")
      break

    else:

      auto.swipe(devices, str(x/ 2), str(y / 3), str(x/ 2), str(y / 6), random.choice(random_ms))
      pass

    minute = random.randint(delay_watch-1, delay_watch)
    time.sleep(minute)
    random_list = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]
    random_percent = random.choice(random_list)

    if react >= 1:

      if react_count < react:
        if random_percent == 1:
          print(random_percent)

          auto.tap(devices, str(x/2), str(y/2))
          time.sleep(0.2)
          auto.tap(devices, str(x/2), str(y/2))

          time.sleep(2)

    minute_count += int(minute)

  auto.opendeeplink(devices, "", package)

def add_friend(driver, auto, devices, add, delay, package):

  add_count = 0
  x = auto.resolution(devices, "x")
  y = auto.resolution(devices, "y")

  auto.opendeeplink(devices, "friends/requests_tab", package)
  time.sleep(5)

  try:

    see_all = driver.find_element_by_xpath("//*[@content-desc='Suggestions']")
    if see_all.is_displayed():
      see_all.click()
      print("Suggestions click")

      for i in range(random.randint(2, 5)):
        auto.swipe(devices, str(x/ 2), str(y / 2), str(x/ 2), str(y / 6), "200")
      #auto.opendeeplink(devices, "friends/new_user_promotion")

  except:
    pass
    
  time.sleep(3)

  if add >= 1:

    for i in range(20):

      print(add_count)

      if add_count < add:

        try:

          name_add = driver.page_source
          list_name = re.findall('Add .* as a friend', name_add)
          time.sleep(delay)

          try:

            add_btn = driver.find_element_by_accessibility_id(list_name[0])
            if add_btn.is_displayed():
              print("found add_btn", list_name[0])
              add_count += 1
              add_btn.click()

          except:
            print("not found add_btn")
            pass

        except:
          print("error name_add")
          pass

      else:
        break

  else:
    print("No add")

  try:

    driver.find_element_by_accessibility_id("Back").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("Back").click()

  except:
    pass


def accept_friend(driver, auto, devices, accept, delay, package):
  accept_count = 0

  auto.opendeeplink(devices, "friends/requests/", package)

  time.sleep(5)

  try:

    see_all = driver.find_element_by_xpath("//*[@content-desc='See all' or @content-desc='See All']")
    if see_all.is_displayed():
      print("See all click")
      see_all.click()
      time.sleep(4)

  except:
    pass

  if accept >= 1:

    for i in range(20):

      print(accept_count)

      if accept_count < accept:

        try:

          name = driver.page_source
          list_name = re.findall("Confirm .*'s friend request", name)
          time.sleep(delay)

          try:

            accept_btn = driver.find_element_by_accessibility_id(list_name[0])
            if accept_btn.is_displayed():
              accept_count += 1
              accept_btn.click()

          except:
            break

        except:
          break

      else:
        break

  else:

    print("No accept")

  try:

    driver.find_element_by_accessibility_id("Back").click()
    time.sleep(1)
    driver.find_element_by_accessibility_id("Back").click()

  except:
    pass
#accept_friend(driver, auto, devices, 10, 4)

def read_notification(driver, auto, devices, read, delay, timeout, package):
  read_count = 0

  auto.opendeeplink(devices, "notifications_tab", package)

  time.sleep(4)

  for i in range(10):

    print(read_count)

    if read_count < read:

      time.sleep(delay)

      try:

        noti_btn = driver.find_element_by_xpath(
          '(//android.view.ViewGroup[@content-desc="{0}"])[{1}]'.format("Manage the notification's settings", str(i+1)))
        
        if noti_btn.is_displayed():
          size_noti_y = noti_btn.rect["y"]
          print("y", size_noti_y)
          size_noti_h = noti_btn.size["height"]
          print("size_noti_h", size_noti_h)
          size_noti_click = int(size_noti_y) + int(size_noti_h)
          print(size_noti_click)

          auto.tap(devices, "360", size_noti_click)
          read_count += 1

          time.sleep(timeout)

          auto.keyevent(devices, "4")
          auto.opendeeplink(devices, "notifications_tab", package)

        else:
          print("Not found")

      except:
        print("cannot click")


    else:
      break

  auto.opendeeplink(devices, "", package)
#read_notification(driver, auto, devices, 3, 2, 8)

def view_storie(driver, auto, devices, timeout, package):
  minute_count = 0

  auto.opendeeplink(devices, "", package)

  auto.keyevent(devices, "4")

  time.sleep(4)

  try:

    storie_btn = driver.find_element_by_xpath(
      '//android.view.ViewGroup[@content-desc="Stories"]')
    if storie_btn.is_displayed():
      size_storie_y = storie_btn.rect["y"]
      print("y", size_storie_y)
      size_storie_h = storie_btn.size["height"]
      print("size_noti_h", size_storie_h)
      size_storie2 = int(size_storie_h) / 2
      print("size_noti2", size_storie2)
      size_storie_click = int(size_storie_y) + int(size_storie2)
      print(size_storie_click)

      auto.tap(devices, "360", size_storie_click)

      time.sleep(3)

      while True:

        if int(minute_count) >= timeout:
          print("break")
          break

        auto.tap(devices, "690", "700")

        minute = random.randint(5, 10)
        time.sleep(minute)

        minute_count += int(minute)

      auto.opendeeplink(devices, "feed", package)

    else:

      print("Not Found ele")

  except:
    print("Not found ele2")

  auto.opendeeplink(devices, "", package)


def create_post(driver, auto, devices, pic, post_text, package):

  auto.opendeeplink(devices, "", package)
  time.sleep(3)

  try:

    post_btn = driver.find_element_by_xpath(
      '//android.view.ViewGroup[@content-desc="Make a post on Facebook"]')
    if post_btn.is_displayed():
      print("found post_btn")
      post_btn.click()
      time.sleep(1)

  except:
    print("not found post_btn")

  if pic == 1:

    try:

      pic_btn = driver.find_element_by_xpath(
        '//android.view.ViewGroup[@content-desc="Photo/video"]')
      if pic_btn.is_displayed():
        print("found pic_btn")
        pic_btn.click()
        time.sleep(1)

        click_pic = driver.find_element_by_xpath(
          '(//android.view.ViewGroup[@content-desc="Photo"])[2]')
        if click_pic.is_displayed():
          print("found click_pic")
          click_pic.click()
          time.sleep(1)

    except:
      print("not found pic_btn")

  try:

    send_post_text = driver.find_element_by_xpath(
      '//android.widget.EditText[@index="0"]')
    if send_post_text.is_displayed():
      print("found send_post_text")
      send_post_text.send_keys(post_text)
      time.sleep(1)

      try:

        post_btn1 = driver.find_element_by_xpath(
          '//android.view.ViewGroup[@content-desc="POST"]')
        if post_btn1.is_displayed():
          print("found post_btn1")
          post_btn1.click()

      except:
        post_btn2 = driver.find_element_by_xpath(
          '//android.view.ViewGroup[@content-desc="Post"]')
        if post_btn2.is_displayed():
          print("found post_btn2")
          post_btn2.click()
          time.sleep(4)

  except:
    print("found send_post_text")


def first_login(driver, auto, devices):

  try:

    skip_btn = driver.find_element_by_xpath("//android.widget.Button[@content-desc='Skip' or @content-desc='SKIP']")
    if skip_btn.is_displayed():
      skip_btn.click()

  except:
    pass


  try:

    find_fri = driver.find_element_by_xpath("//android.widget.Button[@text='Get started']")
    if find_fri.is_displayed():
      find_fri.click()

      time.sleep(0.2)

      all_contact = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
      if all_contact.is_displayed():
        all_contact.click()

  except:
    pass

def data_mode_popup(driver, auto, devices):

  time.sleep(5)

  try:

    no_thanks_btn = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc='No Thanks']")
    if no_thanks_btn.is_displayed():
      no_thanks_btn.click()

      time.sleep(2)

      use_data_btn = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc='OK, Use Data']")
      if use_data_btn.is_displayed():
        use_data_btn.click()
        time.sleep(3)

  except:
    pass


def skip_error_pf(driver, auto, devices, package):

  auto.opendeeplink(devices, "profile", package)
  time.sleep(5)

  try:

    go_back_btn = driver.find_element_by_id("android:id/button2")
    if go_back_btn.is_displayed():
      go_back_btn.click()

  except:
    pass



def rotate_hma(driver, auto, devices):

  auto.openPackage(devices, "com.hidemyass.hidemyassprovpn")
  time.sleep(5)

  try:

    reconnect_btn2 = driver.find_element_by_id("com.hidemyass.hidemyassprovpn:id/view_switch")
    status2 = reconnect_btn2.is_displayed()

    if status2 is True:
      print("found reset btn2")
      reconnect_btn2.click()
      time.sleep(2)
      reconnect_btn2.click()
      time.sleep(10)

      try:

        ip_value = driver.find_element_by_id("com.hidemyass.hidemyassprovpn:id/new_ip_value")
        if ip_value.is_displayed():

          is_not_change = True

          while is_not_change:

            if ip_value.text == "Obtaining…":

              print("waiting !!")
              time.sleep(2)
            

            else:
              is_not_change = False
              print(ip_value.text)
              auto.keyevent(devices, "3")

      except:
        print("no ip")  
           
  except:

    reconnect_btn1 = driver.find_element_by_id("com.hidemyass.hidemyassprovpn:id/reload_button")
    status1 = reconnect_btn1.is_displayed()

    if status1 is True:
      reconnect_btn1.click()
      print("found reset btn1")
      time.sleep(10)

      try:

          ip_value = driver.find_element_by_id("com.hidemyass.hidemyassprovpn:id/new_ip_value")
          if ip_value.is_displayed():

            is_not_change = True

            while is_not_change:

              if ip_value.text == "Obtaining…":

                print("waiting !!")
                time.sleep(2)
              

              else:
                is_not_change = False
                print(ip_value.text)
                auto.keyevent(devices, "3")

      except:
        print("no ip")




  # except:
  #   print("not found reset btn")
  #   rotate_hma(driver, auto, devices)
  #   pass


def fake_gps(driver, auto, devices):

  auto.openPackage(devices, "com.lexa.fakegps")
  time.sleep(3)

  try:

    menu_btn = driver.find_element_by_xpath("//*[@content-desc='Open navigation drawer']")

    if menu_btn.is_displayed():
      menu_btn.click()

      fav_btn = driver.find_element_by_id("com.lexa.fakegps:id/menu_favorite")
      if fav_btn.is_displayed():
        fav_btn.click()
        time.sleep(1)

        cord_btn = driver.find_element_by_id("com.lexa.fakegps:id/saved_locations_list")
        if cord_btn.is_displayed():
          cord_btn.click()
          time.sleep(1)

          start_btn = driver.find_element_by_id("com.lexa.fakegps:id/action_start")
          if start_btn.is_displayed():
            start_btn.click()
            print("Start Fake GPS")
            auto.keyevent(devices, "3")


  except:
    print("not found menu")
    auto.keyevent(devices, "3")

def clear_recent_app(auto, devices):

    x = auto.resolution(devices, "x")
    y = auto.resolution(devices, "y")

    auto.keyevent(devices, "KEYCODE_APP_SWITCH")
    time.sleep(0.5)
    auto.swipe(devices, str(x/ 2), str(y / 3), str(x/ 2), str(y / 6), "100")
    time.sleep(1)
    auto.keyevent(devices, "3")


# auto = AutoADB()
# devices = "061302511Q000763"
# k = Driver(devices, 8200)
# driver = k.start_driver()

# while True:

#   time.sleep(3)

#   scroll_reel(driver, auto, devices, react = 2, timeout = 120, delay_watch = 10, package = "com.facebook.katanb")

  # print(react_post(driver, auto, devices, 1, 2.2))
  # rotate_hma(driver, auto, devices)


# auto = AutoADB()
# device_list  = auto.getDevices()

# clear_recent_app(auto, device_list[0])














#def ramdom_funtion():
#
#  random_list = ["add", "accept", "read", "scroll"]
#  random.choice
#
#  if random

