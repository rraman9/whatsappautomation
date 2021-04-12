# Importing the selenium webdriver.
import time

import pyautogui
from selenium import webdriver
# Importing the keys.
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
# Importing wait.
from selenium.webdriver.support.ui import WebDriverWait
# Importing expected_conditions
from selenium.webdriver.support import expected_conditions

# Creating the driver
driver = webdriver.Chrome()
# Opening the url.
driver.get("https://teams.microsoft.com/l/meetup-join/19%3ameeting_ODk1YWMyNjItNDY1NC00YTIwLWE2MmItMGNiNzE1MTk1Njgy"
           "%40thread.v2/0?context=%7b%22Tid%22%3a%225fd10a7a-9625-46f7-b7f9-551a2760c887%22%2c%22Oid%22%3a"
           "%220c8f5f65-1a12-43cd-9b92-d805a692fcfc%22%7d")

try:
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    time.sleep(5)
except:
    pass
