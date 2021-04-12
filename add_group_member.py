import time

import pyautogui


class AddGroupMember:
    def __init__(self, memberList):
        self.memberList = memberList

    def switchScreen(self):
        pyautogui.click(418, 1052)

    def addMember(self):
        # pyautogui.click(255, 259)
        pyautogui.click(817,270)
        for member in self.memberList:
            #pyautogui.keyDown("shift")
            #pyautogui.keyDown("home")
            #pyautogui.keyUp("home")
            #pyautogui.keyUp("shift")
            #pyautogui.hotkey("delete")
            pyautogui.typewrite(member)
            pyautogui.hotkey("enter")
            time.sleep(1)

# memberInput = ["9818283060","9989098189","9820383434","9826054421","7011463389","9911067632","9980595701","9949899999","8826075235","9182660359","9953390799","9011041500","9848984135","9994196032","8082006481","9892233021","9987764123","9673288522","7894794356","9886723901","9711199830","9764034777","9109990283","9818498940","9535990408","9810230819","9080948346","9845367935","9867525717","8826167875","9888847140","9881209992","8380078567","8349999471","9890798769","9490748405","9880430220","8884400432","9845214810","8296325509","9535159229","9008326328","6397458805","9871929402","8050072095","8121872832","9868746179","8779441729","9412750599","9599858514","9311323174","9820532088","9845035120","9880043327","8169275067","9767467638","9811015669","7500500036","9424018779","9017338221","9434002495","9334192448","9869587303","9535277100","9871427548","9901965553","9916438409","9940215124","7988252683","9820121642","4796657159","9811110998","9019162748","9869471415","9738347368","9953535400","9745279875","9999289199","9900204818","9822073198","9822063197","9867376265","9969128647","9933631515","9810853306","8126723890","9224125936","9773110801","9830212222","9769860021","9845479430","9686695472","9999600651","9425540317","9810372064","9867508085","9457530189","8950164084","9898300392","9725037392","9320063032","9830272728","9833002133","9741128628","9899773102","9008348524","9910011159","9818061104","9342247037","9306261236","9845025116","8939664706","9840711885","9819543360","8867465270","9451087936","9930069991","7894424507","9535366368","8796916174","9432368434","9319309294","9946856718","9993333019","9319309294","9820779945","9422038248","9886657432","9885173222","9313464151","9908545912","9137856980","8104512463","8732803669","9167006336","9810057557","9949508811","9886093776","7921875312","9599240980","9423159000","6587214004","9871111906","9958881498","9987688005","9620232409","9341018855","9945578216","8547871704","9604003690","9665380067","9896081707","9810539755","9740166006","8762020627","9969016955","9811144048","9325212481","8056011114","9967552795","9810035151","9880611022","9652006702","9842254936","9810824297","9599803585","9869236124","9818283060","9980201881","8095668324","8939664706","9845025116","8126723890","843939360","7507012319","9930975610","9986587788","9425540317","9868746179","9892801352","9933631515","9810539755","9325212481","9633167322","9999600651","8779441729","9457530189","9986248546","9980201881","9599240980","9643840720","9886723901","9811910947","9604003690","9745279875","9008326328","9953535400","9620232409","9342247037","9873666127"]  # Input: 7011040802 9313876651

memberInput = ["Anup Das Mandala Vatika Participant","Anusha PV Mandala Vatika Participant","Archana Jha Mandala Vatika Participant","bandi","Chandradhar Tegginmath Mandala Vatika Participant","Chandrashekhar Baghel Mandala","Chhavi Methi Mandala Vatika Participant","Deepa Reddy Mandala Vatika Participant","DINAL SHAH Mandala Vatika Participant","Aparna Cherla Mandala Vatika Participant","Divya Bajaj Mandala Vatika Participant","Dr Ashita Munjal Mandala Vatika Participant","Dr.Arunabha Mitra Mandala Vatika Participant","Geetanjali garg Mandala Vatika Participant","Geetha Naresh Mandala Vatika Participant","Goutam Ghosh Mandala Vatika Participant","HARSH HARLALKA Mandala Vatika Participant","Harshavardhan Gorakh Mandala Vatika Participant","Hrishikesh Bhat Mandala Vatika Participant","I","Jagruti Mandavkar Mandala Vatika Participant","Jaya Goel Mandala Vatika Participant","Jayashree Jaishankar Mandala Vatika Participant","Kusha Kusha Mandala Vatika Participant","Madhavi Swarup Mandala Vatika Participant","Madhu","MADHUMITA GANGULI Mandala Vatika Participant","Mala Gaur Mandala Vatika Participant","Mandala Vatika Participant 19","Mandala Vatika Participant 23","Mandala Vatika Participant 24","Mandala Vatika Participant 26","Mandala Vatika Participant 27","Mandala Vatika Participant 28","Mandala Vatika Participant 30","Mandala Vatika Participant 31","Mandala Vatika Participant 32","Mandala Vatika Participant 37","Mandala Vatika Participant 39","Mandala Vatika Participant 45","Mandala Vatika Participant 54","Mohit Dhukia AOL","Mridula","Niranjan Rao Mandala Vatika Participant","Pratibha Sankhe Mandala Vatika Participant","Prem Goyal Mandala Vatika Participant","Priya","Puneet Mathur Mandala Vatika Participant","Radhik Kalra Mandala Vatika Participant","Radhika","Rajan Dhebe Mandala Vatika Participant","Rajani","Rajani Vadapalli Mandala Vatika Participant","Rajni Singh Mandala Vatika Participant","Ramesh Muthusamy Mandala Vatika Participant","Ranjit","Ranjita Chavan Mandala Vatika Participant","Rishi Jain Mandala Vatika Participant","Ritika Anand Mandala Vatika Participant","Ruchika Elwadhi Mandala Vatika Participant","Saaniya Poddar Mandala Vatika Participant","Sarika Nipunage Mandala Vatika Participant","Sarrika Student Mandala Vatika Participant","Shailesh kumar Kavi Mandala Vatika Participant","Shanmugapriya M Mandala Vatika Participant","Sharmila Bose Mandala Vatika Participant","Shavina Prakash Mandala Vatika Participant","Shiva Kotikalapudi Mandala Vatika Participant","Shobha Swaminathan Mandala Vatika Participant","SUDHIR","Sujata Jain Mandala Vatika Participant","Sukeerti Shukla Mandala Vatika Participant","Sulekha Das Mandala Vatika Participant","SUMAN MITAL Mandala Vatika Participant","Surbhi agrawal PANDE Mandala Vatika Participant","Usharani U.R Mandala Vatika Participant","Vandana Sachdev Mandala Vatika Participant","Vipul Bhaskar Mandala Vatika Participant"]
Bot = AddGroupMember(memberInput)
Bot.switchScreen()
pyautogui.sleep(2)
Bot.addMember()
