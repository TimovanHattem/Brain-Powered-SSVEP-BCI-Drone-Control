import os
import time
import numpy as np
import pandas as pd
from drone import Drone

MAPPING = { '1': 'takeoff',
            '2': 'land',
            '3': 'forward',
            '4': 'backward',
            '5': 'rotate_left',
            '6': 'rotate_right'}
DRONE = None
route_list = [] #None
route_index = 0

# error, land
def handle_signint(signum, frame):
    DRONE.land()

""""""
def read_delete_when_available(filename):
    while not os.path.exists(filename):
        time.sleep(0.05)
    time.sleep(0.1)
    data = np.loadtxt(filename)
    while True:
        try:
            os.remove(filename)
            break
        except:
            continue
    return int(data)


def periodically_classify(route_index=None, route_list=None, filename='prediction.txt'):
    while True:
        command = read_delete_when_available(filename)
        move_drone(command,route_index,route_list)


def move_drone(command,route_index=None,route_list=None):
    if 0 < command < 7:
        print("Predicted {}".format(MAPPING[str(command)]))
        # route_index += 1
        if DRONE != None:
            print("Moving drone!")
            # print(MAPPING[command]) # dit is alleen printen hoe hij zou bewegen
            # hier onder is daadwerkelijk bewegen
            DRONE.move(MAPPING[str(command)])
            # if route_list:
            #     if route_list[route_index] == command:
            #         DRONE.move(MAPPING[str(command)])
        time.sleep(4)
        return True
    else:
        print("No classification")
    time.sleep(4)
    return False

if __name__ == '__main__':
    try:
        DRONE = Drone()
        print("Classifying each second")
        # DRONE.takeoff()
        periodically_classify(route_index, route_list)
    except Exception as e:
        print(e)
        # handle_signint(1, 1)
