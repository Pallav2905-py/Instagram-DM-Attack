'''Author: Pallav'''

#Defined Functions:-
def key_enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

#External Module Imporing:-
from curses import raw
from webbot import *
import time
from pynput.keyboard import Controller, Key

#Code

#User Inputs:-
print("Few Instructions Befor Going Ahead\n1] This software is only for fun purposes any use of this in any trolling purposes can lead to a legal action \n2] Once the attack starts minimum time is 1Min[60 secs] and maximum time is 9Min[9x60 secs] \n3] All the data is stored in your local computer and not on any server so its highly secure \n4] You need to follow the person you want to attack with the account with which you want to send the attack \n4] We do not violet any terms&conditions of instagram by making this bot \n5] Enter few details and then sit back and see your victim getting spammed (: ; have FUN!! ")
time.sleep(1)
agree = input("\n\n\nDid you read all the above instructions? [Y/N]:- ")
print("We need some information about your account before we proceed, remember anything you enter is only seen by you and saved on your local computer and highly secure")
time.sleep(3)
victm_acc_url = input("Enter Victim's account URL \n(eg- www.instagram.com/abcxyz):- ")
sender_acc_id = input("Enter Your Account Login ID \n[By which you want to send attack (we recommand to use a alt account for this)]\n(eg-John Marshall):- ")
time.sleep(1)
sender_acc_pass = input("Enter Your Account Login Password \n[By which you want to send attack (we recommand to use a alt account for this)]\n(eg-123404321):- ")
raw_attack_time = input("Enter For how many seconds you want to send the attack in seconds:- ")
attack_time = int(raw_attack_time)
#Usage of inputs for attack:-
keyboard = Controller()
web = webbot.Browser()
web.go_to("https://www.instagram.com/")
time.sleep(1)
web.click("Phone")
web.type("the_pro_dev")
web.click("password")
web.type("Pallav2@@5")
key_enter()
time.sleep(3)
for i in range(0,2):
    web.click("Not now")
    time.sleep(3)
web.go_to(victm_acc_url)
time.sleep(2)
web.click("Message")
time.sleep(2)
i = 1

time_duration = 10
time_start = time.time()

while time.time() < time_start + time_duration:
    web.type("Hey, you mother fucking BOT!!!\n")
    i = i + 1
    print(i)


