import can
import threading
import sys
import keyboard
import time
import os

shutdown_event = threading.Event()
event_print = True
event_send_mesage = True

print_str = "start"

bus = can.interface.Bus(bustype='slcan', channel='COM9', bitrate=500000,)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dowork():
    global print_str
    while event_print:
        # print(print_str, end="\r" )
        time.sleep(0.5)

mesages_1 = can.Message(arbitration_id=0x7e0,
                          data=[0x03, 0x22, 0x60, 0x1f, 0, 0, 0, 0],
                          is_extended_id=False)                       # odometer request

mesages_2 = can.Message(arbitration_id=0x7e0,
                          data=[0x03, 0x22, 0x60, 0xfa, 0, 0, 0, 0],
                          is_extended_id=False)                        # engine running / not Running

mesages_3 = can.Message(arbitration_id=0x7e0,
                          data=[0x03, 0x22, 0x50, 0x04, 0, 0, 0, 0],
                          is_extended_id=False)                        # Speed request

mesages = [mesages_1, mesages_2, mesages_3]

def send_reqest():
    i=0
    while event_send_mesage:
        time.sleep(1)
        msg = mesages[i]
        i = i + 1
        if i > len(mesages)-1:
            i = 0

        try:
            bus.send(msg)
            # print("Message sent on {}".format(bus.channel_info))
        except can.CanError:
            print("Message NOT sent")

t = threading.Thread(target=dowork, args=(), name='worker')
t.start()
sender = threading.Thread(target=send_reqest, args=(), name='sender')
sender.start()



def get_bit(msg):

    bytes_as_string = msg.data.hex()
    byte_as_list = list(bytes_as_string[i:i + 2] for i in range(0, len(bytes_as_string), 2))
    bite_list = list("{0:08b}".format(int(byte_as_list[i], 16)) for i in range(0, len(byte_as_list), 1))
    mesage = "id:" + str(hex(msg.arbitration_id)) + "  " + str(byte_as_list) + "  " + str(bite_list)
    return byte_as_list

def linear( x , in_min, in_max, out_min, out_max):
    return int((x - in_min)* (out_max-out_min)/(in_max-in_min)+out_min)

def monitor_one_id():
    # try:
    global print_str
    msg = bus.recv(0.1)
    if msg is not None:

        id_to_mon = "7e8"
        id_to_mon = int(id_to_mon, 16)
        if msg.arbitration_id == id_to_mon:
            baytposition = 7
            # data = int(get_bit(msg=msg)[baytposition], 16)
            data = get_bit(msg=msg)
            if data[2] == "60" and data[3] == "1f":
                odometer = int("".join(data[4:8]),16) *2
                print("odometer Km:" + str(odometer))

            if data[2] == "50" and data[3] == "04":
                speed = int(data[4],16)
                print("speed KM/h:" + str(speed))

            if data[2] == "60" and data[3] == "FA":
                eng_staus = int(data[4], 16)
                print("engine status:" + str(eng_staus))


    # print_str=str(str( "C:"+str(ambiant_tempe)+", "+str(ignStatus) + " , " + str(window_washer_status)+ " , " + str(kapota_statuss) + \
    #       " , " + str(bremzhu_pedala_statuss)) )


soft_runing = True
print()
print()
while soft_runing :
    # print("lol")

    try:
        monitor_one_id()
    except KeyboardInterrupt:
        print("id not exist", end="\r")
        event_print = False
        event_send_mesage = False
        shutdown_event.clear()
        soft_runing = False
        break
print("bye")