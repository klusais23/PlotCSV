import can
import sys
import threading
import os
import keyboard
import time
import msvcrt

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

all_id_list = list()


bus = can.interface.Bus(bustype='slcan', channel='COM9', bitrate=250000,)


program_runing = True

def printHeder():
    print()
    print("________________________________________________________________________________")
    print("input R: to real monitoring ,input M: to monitor one ID "\
          " , input E: to exit app , input I: to get all ID ")
    print("________________________________________________________________________________")
    print()

def reallDataMonitorAll():
    try:
        while True:
            msg = bus.recv(1)
            if msg is not None:
                print(msg)

    except KeyboardInterrupt:
        print("stop")
        return None

def monitor_one_id(id=0x00):

    try:

        while True:
            msg = bus.recv()
            if msg is not None:

                if msg.arbitration_id not in all_id_list:
                    all_id_list.append(msg.arbitration_id)

                if msg.arbitration_id == id:

                    bytes_as_string  = msg.data.hex()
                    byte_as_list = list(bytes_as_string[i:i + 2] for i in range(0, len(bytes_as_string), 2))
                    bite_list = list("{0:08b}".format(int(byte_as_list[i], 16)) for i in range(0, len(byte_as_list), 1))

                    mesage = "id:" + str(hex(msg.arbitration_id)) + "  " + str(byte_as_list) +"  "  + str(bite_list)
                    print(mesage, end="\r")

                    # time.sleep(0.1)

    except KeyboardInterrupt:
        print("id not exist", end="\r")
        return None


def get_all_id():
    try:
        while True:
            msg = bus.recv(1)
            if msg is not None:
                if msg.arbitration_id not in all_id_list:
                    all_id_list.append(msg.arbitration_id)

    except KeyboardInterrupt:
        print(all_id_list)
        print("stop")
        return None



while program_runing:

    printHeder()
    comand = input("enter comand: ")

    if comand == "R":
        reallDataMonitorAll()

    if comand == "I":
        print(all_id_list)
        # get_all_id()

    if comand == "M":

        id_to_mon =input("input id: ")
        id_to_mon = int(id_to_mon, 16)
        is_monitoring = True
        id_from_list =len(all_id_list)-1# 0 #all_id_list.index(id_to_mon)
        while is_monitoring:
            monitor_one_id(id_to_mon)
            cls()
            comand_for_moitor = input("E: exit , Non: next: ")
            if comand_for_moitor == "":

                id_to_mon = all_id_list[id_from_list]
                id_from_list = id_from_list - 1
                # cls()
                if id_from_list < 0:
                    id_from_list=len(all_id_list)-1
            elif comand_for_moitor == "E":
                is_monitoring = False

    if comand == "E":
        print("exit")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


