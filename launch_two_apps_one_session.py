from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
desired_caps = {
    "deviceName": "Galaxy S20",
    "platformName": "Android",
    "platformVersion": "10",
    "browserName": "Chrome",
    "app":"lt://APP10160591891685101090430535", #basically this will launch first then other apps will run
    "otherApps":["lt://APP1016039251685508143549205"], #we can pass over three apps in the other app and this will first install the app in "app" and then it will install the other app
    "isRealMobile": True,                               
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "visual": True,
    "video": True,
    "exported":True
}

driver_1= webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  "ritamg"+":"+"e4vXxk64hYOIkG7gwld5Fsb5LpmhI8wq6J0LQ2KC9LSgJHc1N5"+"@mobile-hub.lambdatest.com/wd/hub")
driver_1.launch_app()
driver_1.find_element_by_id("com.lambdatest.proverbial:id/speedTest").click()
time.sleep(5)
driver_1.close_app() # ---> Terminates  the app
#driver_1.activate_app(app_id) #-->"Pass on the build id"
driver_1.activate_app("com.makemytrip") 
driver_1.reset() #-->Resets the app
driver_1.find_element_by_id("com.makemytrip:id/continueButton").click()
time.sleep(5)
driver_1.close_app() #---> Terminates the app
#driver_1.start_activity("com.makemytrip","com.makemytrip.permission.MIPUSH_RECEIVE")
driver_1.close_app()
driver_1.quit()#-->quits the driver