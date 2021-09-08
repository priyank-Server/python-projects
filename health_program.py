#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio
import time

from pygame import *
from datetime import datetime
from time import *

from time import *
from pygame import mixer

# for live time counter
# current_time = datetime.now()
# work_start_time = '09:00:00'
# work_end_time = '17:00:00'

# for calculate amount of water
# water_limit = 3500 # in ml
# glass_size = 200 # in ml
# no_of_glass = round(water_limit / glass_size)


# this is for log

def gettime():
    import datetime
    return datetime.datetime.now()


# this is for music
def music_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a = input("type 'stop' when you done the task :")
        if a == stopper:
            mixer.music.stop()
            break

# if __name__ == '__main__':
#     music_loop("win.mp3", "stop")


# this is for water reminder
def water():
    time.sleep(40*60)
    print("drink one glass of water ")
    music_loop("win.mp3", "stop")
    with open("health_counter.txt", "a") as f:
        f.write(str([str(gettime())]) + ' ' + "water 200ml" + "\n")


# this is for eyes relax reminder
def eyes():
    time.sleep(30*60)
    print("plz relax your eyes for sometime ")
    music_loop("win.mp3", "stop")
    with open("health_counter.txt", "a") as f:
        f.write(str([str(gettime())]) + ' ' + "eye relaxed" + "\n")

# this is for physical activity
def walk():
    time.sleep(45*60)
    print("plz talk a walk ")
    music_loop("win.mp3", "stop")
    with open("health_counter.txt", "a") as f:
        f.write(str([str(gettime())]) + ' ' + "walk" + "\n")


water_amount = 0
while water_amount <= 3600:
    if water_amount == 3600:
        print("you completed you daily tasks")
        break
    else:
        water()
    water_amount = water_amount + 300

    eyes()
    walk()


# except:
#     print("something went wrong")


