import pyautogui
from time import sleep
from random import randint


def typeMessageAndEnter(message):
    pyautogui.typewrite(message)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('alt')


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
    sleep(randint(1, 3))
    pyautogui.typewrite(contact_element)
    sleep(randint(1, 3))
    pyautogui.hotkey('enter')
    sleep(randint(1, 3))
    pyautogui.click(698, 1011)
    sleep(randint(1, 3))
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    sleep(randint(1, 4))
    typeMessageAndEnter("We request the pleasure of your company at the launch event of iGROW.")
    typeMessageAndEnter("*17th Oct, 5 PM*")
    typeMessageAndEnter("Here is the direct link for ease of access : http://tiny.cc/iGROW")
    typeMessageAndEnter("")
    typeMessageAndEnter("Warmly")
    typeMessageAndEnter("Divya Bajaj")
    typeMessageAndEnter("www.igrowdisc.com")
    pyautogui.typewrite("_Microgreens Simplified_")
    pyautogui.hotkey("enter")

