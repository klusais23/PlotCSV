import can
import sys
import os
import time

# Candlelight firmware on Linux
#bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

# Stock slcan firmware on Linux
#bus = can.interface.Bus(bustype='slcan', channel='/dev/ttyACM0', bitrate=500000)

# Stock slcan firmware on Windows
bus = can.interface.Bus(bustype='slcan', channel='COM9', bitrate=500000)

a = 0
while (1):

    msg = can.Message(arbitration_id=0xc0ffee,
                      data=[0, 25, 0, 1, 3, 1, 4, a],
                      is_extended_id=True)
    time.sleep(0.1)
    a = a+1
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent")



# def make_print_string(list):
#     stringTXT =""
#     for iteam in list:
#         stringTXT = stringTXT + str(hex(iteam.arbitration_id)) + "  " +str(iteam.data) + "\n"
#
#     return  stringTXT
#
# allID = list()
# try:
#     print("while starts:")
#     while True:
#         msg = bus.recv(1)
#         if msg is not None:
#             for mes in allID:
#                 if mes.arbitration_id != msg.arbitration_id:
#                     allID.append(msg)
#
#             a=0
#             for mesage in allID:
#                 if mesage.arbitration_id == msg.arbitration_id:
#                     allID[a]=msg
#                     a=a+1
#
#
#             # if msg.arbitration_id == 0x280:
#             print(make_print_string(allID),end="\r")
#             time.sleep(0.2)
#
# except KeyboardInterrupt:
#     try:
#         sys.exit(0)
#     except SystemExit:
#         os._exit(0)