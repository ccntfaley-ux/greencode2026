import threading
from pynput import keyboard
from python_goto import goto
import os
import time
global ky
al = "b"
global o
prev_key = 0
g = 0
release_time = 0
def on_press(key, injected):
    global al
    
    al = key
def start_loop(detect_key):
    global g
    global start_time
    while g == 0:
        start_time+=1 
        if detect_key in str(al):
            g = 1
        
   
    return(start_time)
        
def on_release(key, injected):
    global release_time
    global prev_key
    prev_key = release_time

    release_time = 0
    
d = 0
start_time = 0
ky = ""
al = 65

trn = 1
nxt = 2
sve = 1
qwerty = ["a","s","d","f","g","h","j","k","l"]
dvorak = ["a","o","e","u","i","d","h","t","n"]
ky = input("What is your keyboard layout qwerty,dvorak [qwerty]")
if ky.lower() != "dvorak" :
    ky = qwerty
else:
    ky = dvorak
mode = input("Captcha or password [password]")

input("press enter when ready to drag (drag one key at a time starting from second row of charaters first to end of letters )")
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
for i in range(9):
    g = 0
    start_loop(ky[i])
    g = 0
    print(start_time)
    while g == 0:
        release_time+=1

        if prev_key:
            print(prev_key)
            g = 1
    pass_name = "start" + str(i)
    exec("%s = %d" % (pass_name, start_time))
    pass_name = "release" + str(i)
    exec("%s = %d" % (pass_name, release_time))

   
    start_time = 0
    prev_key = 0

if mode.lower() == "captcha":
    human_start_number = start1 - start2 + start3 - start4 + start5 - start6 + start7 - start8
    human_release_number = release1 - release2 + release3 - release4 + release5 - release6 + release7 - release8
    if human_start_number >= 100 or human_start_number <= 100:
        if human_release_number >= 100 or human_release_number <= 100:
            print("you are human")
        else:
            print("you are an robot")
    else:
        print("you are an robot")


