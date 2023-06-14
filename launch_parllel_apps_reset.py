from appium import webdriver
from time import sleep
desired_caps_1 = {
    "platformName": "Android",
    "deviceName": "Galaxy S20 Ultra",
    "platformVersion": "10",
    "app": "lt://APP10160591891685101090430535",
    "build": "Rishabh_Appium",
    "name": "App1",
    # "lt_user": "rishabhsinghlambdatest",
    # "lt_key": "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei",
    "isRealMobile": True,
   # "resignApp": False,
    "video":True,
    "visual":True
}
desired_caps_2 = {
    "platformName": "Android",
    "deviceName": "Pixel 3",
    "platformVersion": "9",
    "app": "lt://APP1016045801684934067697603",
    "build": "Rishabh_Appium",
    "name": "App2",
    # "lt_user": "rishabhsinghlambdatest",
    # "lt_key": "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei",
    "isRealMobile": True,
    "video":True,
    "visual":True
}
# Initialize the Appium driver for the first app
driver_1= webdriver.Remote(desired_capabilities=desired_caps_2, command_executor="https://" +
                                  username+":"+access_key+"@mobile-hub.lambdatest.com/wd/hub")
# Launch the first app
driver_1.launch_app()
# Perform actions on the first app
driver_1.close_app()
# Initialize the Appium driver for the second app
driver_2= webdriver.Remote(desired_capabilities=desired_caps_2, command_executor="https://" +
                                  username+":"+access_key+"@mobile-hub.lambdatest.com/wd/hub")
# Launch the second app
driver_2.launch_app()
driver_1.reset()
# Perform actions on the second app
# ...
# Switch back to the first app
#driver_1.activate_app('com.package.firstapp')
# Perform more actions on the first app
# ...
# Switch back to the second app
#driver_2.activate_app('com.package.secondapp')
# Perform more actions on the second app
driver_2.close_app()
driver_1.launch_app()
driver_1.close_app()
# Close the app sessions
driver_1.quit()
driver_2.quit()









