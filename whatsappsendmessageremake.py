import pyautogui
from time import sleep
from random import randint

pyautogui.keyDown('alt')
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')
contact_list = ["7011040802", "9810057557"]
for contact_element in contact_list:
    sleep(randint(1, 10))
    pyautogui.click(100, 110)
    sleep(randint(1, 15))
    pyautogui.typewrite(contact_element)
    sleep(randint(1, 15))
    pyautogui.hotkey('enter')
    sleep(randint(1, 15))
    pyautogui.click(698, 1011)
    sleep(randint(1, 15))
    pyautogui.typewrite("Test message")
    sleep(randint(1, 15))
    pyautogui.hotkey("enter")
