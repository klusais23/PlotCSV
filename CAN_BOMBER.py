import can
import threading
import sys
import keyboard
import time
import os

shutdown_event = threading.Event()
event_print = True
event_send_mesage = True

Response = False

response_mesge = "resp"

bus = can.interface.Bus(bustype='slcan', channel='COM10', bitrate=500000,)

def send_bomber():
    global response_mesge
    global Response
    Start_ID = 0x0
    end_ID = 0x7FF
    mesageSendTimes = 3
    while event_send_mesage:
        time.sleep(0.01)

        for i in range(0,mesageSendTimes,1):
            msg = can.Message(arbitration_id=Start_ID,
                                    data=[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF],
                                    is_extended_id=False)  # odometer request

            bus.send(msg)
            time.sleep(0.03)
        if Response == True:
            Response=False
            response_mesge = msg.arbitration_id
            print(msg.arbitration_id)

        Start_ID = Start_ID + 1

        if Start_ID > end_ID:
            break

        # try:
        #     bus.send(msg)
        #     # print("Message sent on {}".format(bus.channel_info))
        # except can.CanError:
        #     print("Message NOT sent")

# t = threading.Thread(target=dowork, args=(), name='worker')
# t.start()
sender = threading.Thread(target=send_bomber, args=(), name='sender')
sender.start()

def reallDataMonitorAll():
    global response_mesge
    global Response

    msg = bus.recv(1)
    if msg is not None:
        Response = True
        print("Recive_"+str(msg) )


soft_runing = True
print()
print()
while soft_runing :
    # print("lol")

    try:
        reallDataMonitorAll()
    except KeyboardInterrupt:
        print("id not exist", end="\r")
        event_print = False
        event_send_mesage = False
        shutdown_event.clear()
        soft_runing = False
        break
print("bye")