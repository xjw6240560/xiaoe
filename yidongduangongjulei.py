import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",
    "platformVersion": "12",  # adb shell getprop ro.build.version.release
    "deviceName": "127.0.0.1:16384",
    "appPackage": "com.example.sxxm",  # adb shell pm list packages -3 -f
    "appActivity": "com.example.sxxm.View.Dengruzhuce",  # adb shell monkey -p 包名 -v -v -v 1
    "unicodeKeyboard": True,
    "resetKeyboard": True,
}

# 启动app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)
driver.find_element(By.ID, "com.example.sxxm:id/bt2").click()

