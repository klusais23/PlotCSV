import can
import threading
import sys
import keyboard
import time
import os

shutdown_event = threading.Event()
event_is_runing = True

ignStatus =""		        # id:0x20         can B
ambiant_tempe=0             # id:0x339        can B
window_washer_status= ""    # id:0x18ef0900   can B
kapota_statuss = ""         # id:0x337        can B
bremzhu_pedala_statuss = "" # id:0x351        can B

print_str = "start"

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dowork():
    global print_str
    while event_is_runing:
        print(print_str, end="\r" )
        time.sleep(0.5)

t = threading.Thread(target=dowork, args=(), name='worker')
t.start()

bus = can.interface.Bus(bustype='slcan', channel='COM9', bitrate=500000,)

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
    global ignStatus
    global ambiant_tempe
    global window_washer_status
    global kapota_statuss
    global bremzhu_pedala_statuss
    global print_str

    msg = bus.recv(0.1)
    if msg is not None:

        id_to_mon = "20"
        id_to_mon = int(id_to_mon, 16)
        if msg.arbitration_id == id_to_mon:  # ignStatus =""		        # id:0x20         can B
            baytposition = 3
            data = int(get_bit(msg=msg)[baytposition], 16)
            if data & 0x10:
                ignStatus = "ign_ON"
            else:
                ignStatus = "ign_OFF"


        id_to_mon = "18ef0900"
        id_to_mon = int(id_to_mon, 16)
        if msg.arbitration_id ==id_to_mon:  # window_washer_status= ""    # id:0x18ef0900   can B
            baytposition = 7
            data = int(get_bit(msg=msg)[baytposition], 16)
            if data & 0x1:
                window_washer_status = "washer_OFF"
            else:
                window_washer_status = "washer_ON"


        id_to_mon = "337"
        id_to_mon = int(id_to_mon, 16)
        if msg.arbitration_id == id_to_mon:  # kapota_statuss = ""         # id:0x337        can B
            baytposition = 0
            data = int(get_bit(msg=msg)[baytposition], 16)
            if data & 0x10:
                kapota_statuss = "hood_closed"
            else:
                kapota_statuss = "hood_open"


        id_to_mon = "351"
        id_to_mon = int(id_to_mon, 16)
        if msg.arbitration_id == id_to_mon:  # bremzhu_pedala_statuss = "" # id:0x351        can B
            baytposition = 1
            data = int(get_bit(msg=msg)[baytposition], 16)
            if data & 0x20:
                bremzhu_pedala_statuss = "brake_PREST"
            else:
                bremzhu_pedala_statuss = "brake_RELASE"

        id_to_mon = "339"
        id_to_mon = int(id_to_mon, 16)
        if msg.arbitration_id == id_to_mon:  #ambiant_tempe=0  # id:0x339   can B
            baytposition = 2
            data = int(get_bit(msg=msg)[baytposition], 16)
            ambiant_tempe = linear(x=data, in_min=84 , in_max=247, out_min=2 , out_max=84)



    print_str=str(str( "C:"+str(ambiant_tempe)+", "+str(ignStatus) + " , " + str(window_washer_status)+ " , " + str(kapota_statuss) + \
          " , " + str(bremzhu_pedala_statuss)) )

    # except KeyboardInterrupt:
    #     print("id not exist", end="\r")
    #     return None
soft_runing = True
print()
print()
while soft_runing :
    # print("lol")

    try:
        monitor_one_id()
    except KeyboardInterrupt:
        print("id not exist", end="\r")
        event_is_runing = False
        shutdown_event.clear()
        soft_runing = False
        break
print("bye")