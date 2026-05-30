# start here
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
input("press enter when ready to drag (drag starting/n from second row of charaters first to end of letters )")
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
start_loop(ky[0])
if prev_key:
    print(prev_key)
