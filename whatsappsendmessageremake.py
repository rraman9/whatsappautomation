import pyautogui
from time import sleep
from random import randint

pyautogui.keyDown('alt')
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')
contact_list = []
for contact_element in contact_list:
    sleep(randint(1, 10))
    pyautogui.click(100, 110)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    pyautogui.hotkey('delete')
    sleep(randint(1, 15))
    pyautogui.typewrite(contact_element)
    sleep(randint(1, 15))
    pyautogui.hotkey('enter')
    sleep(randint(1, 15))
    pyautogui.click(698, 1011)
    sleep(randint(1, 15))
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    sleep(randint(1, 15))
    pyautogui.typewrite("*Experience meditation* by registering for this free session at https://tiny.cc/whymeditate1 - see you soon! Please also pass it on to family and friends who may benefit from meditation")
    pyautogui.hotkey("enter")
