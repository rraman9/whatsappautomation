import time

import pyautogui


class AddGroupMember:
    def __init__(self, memberList):
        self.memberList = memberList

    def switchScreen(self):
        pyautogui.click(418, 1052)

    def addMember(self,member):
        # Click add participant
        pyautogui.click(1393, 894)

        # Click on the text box for entry of contact name
        pyautogui.click(939, 271)
        # Typing member name
        pyautogui.typewrite(member)
        time.sleep(1)
        pyautogui.hotkey("enter")
        # Click on tick mark
        time.sleep(2)
        pyautogui.click(1118, 866)
        # Waiting to see if invitation dialog comes up
        pyautogui.click(1065, 600)
        time.sleep(3)

        #time.sleep(10)

    def addMembers(self):
        # pyautogui.click(255, 259)
        # Click on "Add member"

        for member in self.memberList:
            self.addMember(member)


memberInput = ["Sushmita Kapoor Mandala Vatika Participant","Vaibhavi Bandekar Mandala Vatika Participant","Vamsi Krishna V Mandala Vatika Participant","Vikas Saraswat Mandala Vatika Participant","Vikas Sharma Mandala Vatika Participant","Vipul Bhaskar Mandala Vatika Participant","Vishwa Bhalekar Mandala Vatika Participant","Vlatka Klanjcic-Rawat Mandala Vatika Participant"]
Bot = AddGroupMember(memberInput)
Bot.switchScreen()
pyautogui.sleep(2)
Bot.addMembers()
