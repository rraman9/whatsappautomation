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

contact_list = [

]

print("original list: " + str(len(contact_list)))
contact_list_without_chars = []
for contact in contact_list:
    contactNew = contact.replace(" ", "")
    contactNew = contactNew.replace("\(", "")
    contactNew = contactNew.replace("\)", "")
    contact_list_without_chars.append(contactNew)

contact_list_without_duplicates = list(dict.fromkeys(contact_list_without_chars))
print("final list: " + str(len(contact_list_without_duplicates)))


def paste_item_from_clipboard_save_list(item_number):
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('v')
    sleep(randint(1, 2))
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('v')
    sleep(randint(1, 2))
    # text message
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')
    pyautogui.keyDown('h')
    pyautogui.keyUp('h')
    sleep(randint(1, 2))
    for i in range(item_number):
        pyautogui.keyDown('down')
        pyautogui.keyUp('down')
    pyautogui.hotkey("enter")
    sleep(randint(1, 2))

for contact_element in contact_list_without_duplicates:
    sleep(randint(1, 2))
    #pyautogui.click(322, 225)  # small monitor real whatsapp
    #pyautogui.click(258, 580)  # small monitor w9673338752eb whatsapp with disconnected phone
    #pyautogui.click(250,370) # small monitor web whatsapp
    #pyautogui.click(198,242) # AWS workspace on small monitor with disconnected phone
    #pyautogui.click(196,160) # AWS workspace on small monitor with connected phone
    pyautogui.click(418, 294)  # AWS workspace on big monitor with disconnected phone
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    pyautogui.hotkey('delete')

    sleep(randint(1, 2))
    pyautogui.typewrite(contact_element)
    sleep(randint(1, 2))
    pyautogui.hotkey('enter')
    sleep(randint(1, 2))
    # pyautogui.click(698, 1011)
    # Image
    paste_item_from_clipboard_save_list(1)
    pyautogui.hotkey('enter')+919881257050

    paste_item_from_clipboard_save_list(2)
    pyautogui.hotkey('enter')


