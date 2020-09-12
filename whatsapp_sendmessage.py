from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time


def send_message_to_contact_from_clipboard(contact, driver):
    # inp_xpath_search = "//input[@title='Search or start new chat']"
    # inp_xpath_search = '//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"][data-tab="3"]'
    # input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    input_box_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_css_selector('div._3FRCZ'))
    input_box_search.click()
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.send_keys("a")
    actions.key_up(Keys.CONTROL)
    actions.send_keys(Keys.DELETE)
    actions.perform()
    input_box_search.send_keys(contact)
    input_box_search.send_keys(Keys.ENTER)
    contactFound = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_css_selector('div.DP7CM')).text
    if contactFound == contact:
        actions.key_down(Keys.CONTROL)
        actions.send_keys("v")
        actions.key_up(Keys.CONTROL)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        input_box_search = WebDriverWait(driver, 50).until(
            lambda driver: driver.find_element_by_css_selector('div._3FRCZ'))
        input_box_search.click()
        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL)
        actions.send_keys("a")
        actions.key_up(Keys.CONTROL)
        actions.send_keys(Keys.DELETE)
        actions.perform()
        #input_box_search.send_keys("On this beautiful occasion of *Teachers' Day* !! \n\n▶️Announcing The most awaited ✨\n✳️ Online Sahaj Samadhi Meditation Program\n with our beloved Bharat Vig ji😇\n\n✳️18thSep - 20th Sep\n(Friday-Sunday)\nTwo batches\n7:30AM-9:30AM\n6:30PM-8:30PM\n\n19,20  Sep Combined batch \n6:30pm to 8:30pm\n\n✳️ Experience deep effortless Meditaton with your personal Mantra.\n\n✳️ Exclusive for 10 participants per batch.\n\n✳️ Eligibility: 16years & Above.\n\n✳️ Register\nMorning 6.30 to 8.30 am (Friday) and Evening 6.30pm to 8.30pm (Saturday, Sunday)\nhttp://aolt.in/499013\n\nEvening 6.30pm to 8.30pm (Friday, Saturday, Sunday)\nhttp://aolt.in/499015\n\nHelpline: 9810057557")
        #input_box_search.send_keys(Keys.ENTER)
        # additionalTextField = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_css_selector('div._3FRCZ copyable-text selectable-text'))
        #actions.send_keys("Join https://artoflivingca.zoom.us/j/4573851235 for a preview into the deep dive course! Don't miss! *Today 11am*")
        #actions.send_keys(Keys.ENTER)
        # actions.perform()


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com")
contact_list = ["Kavita Di AMP 1","Kavita Di AMP 2","Kavita Di AMP 3","Kavita Di AMP 4","Kavita Di AMP 5","Kavita Di AMP 6","Kavita Di AMP 7","Kavita Di AMP 8","Kavita Di AMP 9","Kavita Di AMP 10","Kavita Di AMP 11","Kavita Di AMP 12","Kavita Di AMP 13","Kavita Di AMP 14","Kavita Di AMP 15","Kavita Di AMP 16","Kavita Di AMP 17","Kavita Di AMP 18","Kavita Di AMP 19","Kavita Di AMP 20","Kavita Di AMP 21","Kavita Di AMP 22","Kavita Di AMP 23","Kavita Di AMP 24","Kavita Di AMP 25","Kavita Di AMP 26","Kavita Di AMP 27","Kavita Di AMP 28","Kavita Di AMP 29","Kavita Di AMP 30","Kavita Di AMP 31","Kavita Di AMP 32","Kavita Di AMP 33","Kavita Di AMP 34","Kavita Di AMP 35","Kavita Di AMP 36","Kavita Di AMP 37","Kavita Di AMP 38","Kavita Di AMP 39","Kavita Di AMP 40","Kavita Di AMP 41","Kavita Di AMP 42","Kavita Di AMP 43","Kavita Di AMP 44","Kavita Di AMP 45","Kavita Di AMP 46","Kavita Di AMP 47","Kavita Di AMP 48","Kavita Di AMP 49","Kavita Di AMP 50","Kavita Di AMP 51","Kavita Di AMP 52","Kavita Di AMP 53","Kavita Di AMP 54","Kavita Di AMP 55","Kavita Di AMP 56","Kavita Di AMP 57","Kavita Di AMP 58","Kavita Di AMP 59","Kavita Di AMP 60","Kavita Di AMP 61","Kavita Di AMP 62","Kavita Di AMP 63","Kavita Di AMP 64","Kavita Di AMP 65","Kavita Di AMP 66","Kavita Di AMP 67","Kavita Di AMP 68","Kavita Di AMP 69","Kavita Di AMP 70","Kavita Di AMP 71","Kavita Di AMP 72","Kavita Di AMP 73","Kavita Di AMP 74","Kavita Di AMP 75","Kavita Di AMP 76","Kavita Di AMP 77","Kavita Di AMP 78","Kavita Di AMP 79","Kavita Di AMP 80","Kavita Di AMP 81","Kavita Di AMP 82","Kavita Di AMP 83","Kavita Di AMP 84","Kavita Di AMP 85","Kavita Di AMP 86","Kavita Di AMP 87","Kavita Di AMP 88","Kavita Di AMP 89","Kavita Di AMP 90","Kavita Di AMP 91","Kavita Di AMP 92","Kavita Di AMP 93","Kavita Di AMP 94","Kavita Di AMP 95","Kavita Di AMP 96","Kavita Di AMP 97","Kavita Di AMP 98","Kavita Di AMP 99","Kavita Di AMP 100","Kavita Di AMP 101","Kavita Di AMP 102","Kavita Di AMP 103","Kavita Di AMP 104","Kavita Di AMP 105","Kavita Di AMP 106","Kavita Di AMP 107","Kavita Di AMP 108","Kavita Di AMP 109","Kavita Di AMP 110","Kavita Di AMP 111","Kavita Di AMP 112","Kavita Di AMP 113","Kavita Di AMP 114","Kavita Di AMP 115","Kavita Di AMP 116","Kavita Di AMP 117","Kavita Di AMP 118","Kavita Di AMP 119","Kavita Di AMP 120","Kavita Di AMP 121","Kavita Di AMP 122","Kavita Di AMP 123","Kavita Di AMP 124","Kavita Di AMP 125","Kavita Di AMP 126","Kavita Di AMP 127","Kavita Di AMP 128","Kavita Di AMP 129","Kavita Di AMP 130","Kavita Di AMP 131","Kavita Di AMP 132","Kavita Di AMP 133","Kavita Di AMP 134","Kavita Di AMP 135","Kavita Di AMP 136","Kavita Di AMP 137","Kavita Di AMP 138","Kavita Di AMP 139","Kavita Di AMP 140","Kavita Di AMP 141","Kavita Di AMP 142","Kavita Di AMP 143","Kavita Di AMP 144","Kavita Di AMP 145","Kavita Di AMP 146","Kavita Di AMP 147","Kavita Di AMP 148","Kavita Di AMP 149","Kavita Di AMP 150","Kavita Di AMP 151","Kavita Di AMP 152","Kavita Di AMP 153","Kavita Di AMP 154","Kavita Di AMP 155","Kavita Di AMP 156"]
print("Scan QR Code, And then Enter")
input()
print("Logged In")
for contact in contact_list:
    send_message_to_contact_from_clipboard(contact, driver)
driver.quit()
