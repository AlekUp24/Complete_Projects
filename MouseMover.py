import pyautogui as p
import datetime as d
import random, time

curr_pos = p.position()
width, height = p.size()
time_counter = 0
now = d.datetime.now()

while True:
    
    if p.position() == curr_pos:
        time_counter +=1
    else:
        time_counter = 0
        now = d.datetime.now()
        curr_pos = p.position()

    if time_counter > 10:
        x = random.randint(100,width-100)
        y = random.randint(100,height-100)
        p.moveTo(x,y,0.5)
        curr_pos = p.position()

    end = d.datetime.now() 
    print(f"Last mouse move: {str(abs(now-end))[:7]} s ago...")
    time.sleep(1)
