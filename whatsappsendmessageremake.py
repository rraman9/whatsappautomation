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
    contactNew = contactNew.replace(" ", "")
    contact_list_without_chars.append(contactNew)
contact_list_without_duplicates = list(dict.fromkeys(contact_list_without_chars))
print("final list: " + str(len(contact_list_without_duplicates)))
for contact_element in contact_list_without_duplicates:
    sleep(randint(1, 10))
    pyautogui.click(100, 110)
    # pyautogui.click(277, 196)
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
    typeMessageAndEnter("*FINAL CALL*")
    typeMessageAndEnter(
        "*25 Dec to 27 Dec* (Friday-Sunday). On special occasion of *Mokshada Ekadashi* One of the most auspicious dates!")
    typeMessageAndEnter("Two batches on 25 Dec (11am to 1pm, 6pm to 8pm)")
    typeMessageAndEnter("Combined batch on 26, 27 Dec (6pm to 8pm)")
    typeMessageAndEnter("For 25 morning register http://aolt.in/519539")
    typeMessageAndEnter("For 25 evening register http://aolt.in/519540")
    typeMessageAndEnter("*HURRY* ONLY 10 seats per batch!")
    typeMessageAndEnter(
        "About *Bharat Vig ji* Been with Gurudev since age of 13 and also His secretary for 7 years, taking Sahaj, VTP, TTP, Happiness, DSN and numerous courses, session are going to be *full of learning*")
    typeMessageAndEnter(
        "Feel free to forward to others who haven't done Sahaj or message me if you'd like me to call and follow up with any lead")
    # typeMessageAndEnter("*Meditation* unlocks all success in life!")
    # typeMessageAndEnter("Today 6:30pm - soak yourself in meditation - experience live!")
    # typeMessageAndEnter("Register here to get a zoom link: http://tiny.cc/whymeditate1")
    # typeMessageAndEnter("Please do forward to friends and family who are interested in learning meditation")
    # typeMessageAndEnter("Register for the *FREE* session by clicking on http://tiny.cc/managemytime. Session is facilitated by *Bharat Vig* ji, who is an Art of Living teacher for more than 2 decades!")
    # typeMessageAndEnter("Please do forward to friends and family who are interested in learning about the wonderful skill of time management!")
    # typeMessageAndEnter("Jai Gurudev! If you have missed doing Sahaj earlier, or you want to have someone you know do it, here's an excellent chance!!")
    # typeMessageAndEnter("Two batches on 25 Dec (11am to 1pm, 6pm to 8pm)")
    # typeMessageAndEnter("Combined batch on 26, 27 Dec (6pm to 8pm)")
    # typeMessageAndEnter("For 25 morning register http://aolt.in/519539")
    # typeMessageAndEnter("For 25 evening register http://aolt.in/519540")
    # typeMessageAndEnter("*HURRY* ONLY 10 seats per batch!")
    # typeMessageAndEnter("About *Bharat Vig ji* Been with Gurudev since age of 13 and also His secretary for 7 years, taking Sahaj, VTP, TTP, Happiness, DSN and numerous courses, session are going to be *full of learning*")
    # typeMessageAndEnter("*Meditation* unlocks all success in life!")
    # typeMessageAndEnter("Jai Gurudev! Bharat Vig Ji is an entrepreneur, AOL teacher for 20+ years, teaches VTP, TTP, Sahaj and numerous courses and has been Gurudev's secretary for over 7 years!")
    # typeMessageAndEnter("Join him to learn about time management this Sunday 20 Dec by clicking on http://tiny.cc/managemytime. Please do forward to friends and family who are interested in learning about the wonderful skill of time management!")
    # typeMessageAndEnter("We wish to achieve so much in life, but time, days, years are just slipping away! ")
    # typeMessageAndEnter("Isn't it? ")
    # typeMessageAndEnter("Wouldn't it be nice if we knew how to accomplish more in a given timespan....")
    # typeMessageAndEnter("Learn the life-hacks, tips & easy to adopt techniques in this Free Masterclass with none other than *Bharat Vig* ji!")
    # typeMessageAndEnter("Today (Sunday) *1pm to 2pm*")
    # typeMessageAndEnter("Register here : http://tiny.cc/managemytime and also forward to friends and family (specially students) who want to learn time management!")
    pyautogui.hotkey("enter")
