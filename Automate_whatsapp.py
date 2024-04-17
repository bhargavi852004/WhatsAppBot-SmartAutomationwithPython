import pywhatkit
import time
#sending whatsapp message at 8:30 Am :- sendmsg("Receiver Phone number along with nui code","message","hour","minutes")
pywhatkit.sendwhatmsg("+91XXXXXXXXXX","hello world;its an automate message",8,30)
#sending image via whatsapp to a specific number
pywhatkit.sendwhats_image("+91XXXXXXXXXX","hello.png",caption="hiii",wait_time=1,tab_close=True,close_time=3)
#sending whatsapp message to a specific group at 12A.M
pywhatkit.sendwhatmsg_to_group("group name","hey all!",0,0)
#sending image via whatsapp to a specific group
pywhatkit.sendwhats_image("groupname","hello.png","hii")
# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("groupname","hii")
# Send message to a specific contact but Closes the Tab in 3 Seconds after waiting for 15 seconds Sending the Message
pywhatkit.sendwhatmsg("+91XXXXXXXXXX", "Hi", 0, 0,15, True, 3)
# To Play a Video on YouTube playonyt("topic name")
pywhatkit.playonyt("whatsapp")
# To search for a keyword in Google search
pywhatkit.search("whatsapp")
#To get information about a particular topic pywhatkit.info(“pagename”,lines=x)
pywhatkit.info("pagename", lines = 5)
