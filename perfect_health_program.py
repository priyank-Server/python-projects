from datetime import datetime
from pygame import mixer
from time import*


def music_play(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("perfect_health_counter.txt", "a") as f:
        f.write(f"{msg} " + str([str(datetime.now())]) + "\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_walk = time()
    water_sec = 10
    eyes_sec = 30*60
    walk_sec = 45*60

    while True:
        if time() - init_water > water_sec:
            print("Water Drinking Time. Enter 'done' to stop the alarm :")
            music_play("win.mp3", "done")
            init_water = time()
            log_now("Drank Water at :")

        if time() - init_eyes > eyes_sec:
            print("Eyes Relaxation Time. Enter 'done' to stop the alarm :")
            music_play("win.mp3", "done")
            init_eyes = time()
            log_now("Eyes Relaxed at :")

        if time() - init_walk > walk_sec:
            print("Walking Time. Enter 'done' to stop the alarm :")
            music_play("win.mp3", "done")
            init_walk = time()
            log_now("Talk a walk :")

