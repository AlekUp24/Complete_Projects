import pyautogui as p
import random, time

curr_pos = p.position()
time_counter = 0

while True:
    
    if p.position() == curr_pos:
        time_counter +=1
    else:
        time_counter = 0
        curr_pos = p.position()

    if time_counter > 10:
        x = random.randint(100,1000)
        y = random.randint(100,1000)
        p.moveTo(x,y,0.5)
        curr_pos = p.position()

    print(f"Last mouse move: {time_counter} s ago...")
    time.sleep(1)
