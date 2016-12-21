#!E:\Study\Python\Appium\PS\Demo.py
# -*- coding: UTF-8 -*-
import  time
waittime = 1
pakacage = 'com.bana.dating'

class Register1Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.wait_activity(pakacage + '.splash.activity.SplashActivity',10,1)
        time.sleep(waittime)

    def click