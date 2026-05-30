# start here
import threading
from pynput import keyboard
from python_goto import goto
import os
import time
global ky
al = "b"
global o
def on_press(key, injected):
    global al
    
    al = key
    
        
def on_release(key, injected):
    print('{} released; it was {}'.format(
        key, 'faked' if injected else 'not faked'))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
d = 0
start_time = 0
ky = ""
al = 65
g = 0
trn = 1
nxt = 2
sve = 1
qwerty = ["a","s","d","f","g","h","j","k","l"]

ky = input("What is your keyboard layout qwerty [qwerty]")
if ky.lower() != "qwerty":
    ky = "qwerty"
input("press enter when ready to drag (drag starting/n from second row of charaters first to end of letters )")
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
while g == 0:
    start_time+=1 
    if "a" in str(al):
        g = 1
        print("dhue")
    else:
        print(al)
        
        
   

print(start_time)
