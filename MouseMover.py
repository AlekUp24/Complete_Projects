import pyautogui as p
import datetime as d
import random, time


def write_log(curr, new):
    curr , new = str(curr) , str(new)
    file_path = "C:\\Users\\hubi4\\Desktop\\Hubert.txt" 
    log_file = open(file_path,'a')
    log_file.write(F"Position changed from {curr} to {new} \n")
    log_file.close()


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
        z = random.uniform(0.3,1.5) # randomize mouse speed
        p.moveTo(x,y,z)
        try:
            write_log(curr_pos , p.position())
        except:
            print("couldn't log to the file")
        curr_pos = p.position()

    end = d.datetime.now() 
    print(f"Last mouse move: {str(abs(now-end))[:7]} s ago...")
    time.sleep(1)
