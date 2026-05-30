
from pynput import keyboard
from python_goto import goto
global ky
al = "b"
global o
prev_key = 0
g = 0
total_check = 0
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

input("press enter when ready to press (press one key at a time starting from second row of charaters first to end of letters )")
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
for i in range(9):
    g = 0
    start_loop(ky[i])
    g = 0
   
    while g == 0:
        release_time+=1

        if prev_key:
            
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
    SystemExit

range0 = [start0-400000,start0 + 400000]
range1 = [start1-400000,start1 + 400000]
range2 = [start2-400000,start2 + 400000]
range3 = [start3-400000,start3 + 400000]
range4 = [start4-400000,start4 + 400000]
range5 = [start5-400000,start5 + 400000]
range6 = [start6-400000,start6 + 400000]
range7 = [start7-400000,start7 + 400000]
range8 = [start8-400000,start8 + 400000]
brange0 = [release0-400000,release0 + 400000]
brange1 = [release1-400000,release1 + 400000]
brange2 = [release2-400000,release2 + 400000]
brange3 = [release3-400000,release3 + 400000]
brange4 = [release4-400000,release4 + 400000]
brange5 = [release5-400000,release5 + 400000]
brange6 = [release6-400000,release6 + 400000]
brange7 = [release7-400000,release7 + 400000]
brange8 = [release8-400000,release8 + 400000]
print("password mode, please enter password")
input("press enter when ready to press (press? one key at a time starting from second row of charaters first to end of letters )")
for i in range(9):
    g = 0
    start_loop(ky[i])
    g = 0
    
    while g == 0:
        release_time+=1

        if prev_key:
            
            g = 1
    pass_name = "start" + str(i)
    exec("%s = %d" % (pass_name, start_time))
    pass_name = "release" + str(i)
    exec("%s = %d" % (pass_name, release_time))

   
    start_time = 0
    prev_key = 0
if start0 >= range0[0] and start0 <= range0[1]:
    total_check += 1
if start1 >= range1[0] and start1 <= range1[1]:
    total_check += 1
if start2 >= range2[0] and start2 <= range2[1]:
    total_check += 1
if start3 >= range3[0] and start3 <= range3[1]:
    total_check += 1
if start4 >= range4[0] and start4 <= range4[1]:
    total_check += 1
if start5 >= range5[0] and start5 <= range5[1]:
    total_check += 1
if start6 >= range6[0] and start6 <= range6[1]:
    total_check += 1
if start7 >= range7[0] and start7 <= range7[1]:
    total_check += 1
if start8 >= range8[0] and start8 <= range8[1]:
    total_check += 1
if release0 >= brange0[0] and release0 <= brange0[1]:
    total_check += 1
if release1 >= brange1[0] and release1 <= brange1[1]:
    total_check += 1
if release2 >= brange2[0] and release2 <= brange2[1]:
    total_check += 1
if release3 >= brange3[0] and release3 <= brange3[1]:
    total_check += 1
if release4 >= brange4[0] and release4 <= brange4[1]:
    total_check += 1
if release5 >= brange5[0] and release5 <= brange5[1]:
    total_check += 1
if release6 >= brange6[0] and release6 <= brange6[1]:
    total_check += 1
if release7 >= brange7[0] and release7 <= brange7[1]:
    total_check += 1
if release8 >= brange8[0] and release8 <= brange8[1]:
    total_check += 1

if total_check >= 14:
    print("user verified")
    input()
    total_check = 0
    goto(line=103)
else:
    input("incorrect")
    total_check = 0
    goto(line=104)

        

        
