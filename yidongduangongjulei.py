from appium import webdriver
desired_caps = {
 "platformName": "Android",
 "platformVersion": "7.1.2", #adb shell getprop ro.build.version.release
 "deviceName": "127.0.0.1:21503",
 "appPackage": "com.tencent.mm", #adb shell pm list packages -3 -f
 "appActivity": "com.tencent.mm.ui.LauncherUI", #abd shell monkey -p 包名 -v -v -v 1
 "unicodeKeyboard": True,
 "resetKeyboard": True,
}

# 启动app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

