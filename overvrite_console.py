import sys
import time
import can
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

bus = can.interface.Bus(bustype='slcan', channel='COM10', bitrate=500000,)
print("conected :)")

def monitor_one_id(id=0x00):

    try:

        while True:
            msg = bus.recv()
            if msg is not None:
                if msg.arbitration_id == id:
                    bytes_as_string  = msg.data.hex()
                    byte_as_list = list(bytes_as_string[i:i + 2] for i in range(0, len(bytes_as_string), 2))
                    bite_list = list("{0:08b}".format(int(byte_as_list[i], 16)) for i in range(0, len(byte_as_list), 1))
                    string = str("0x"+ byte_as_list[0])
                    a = int(string,16)
                    print_percent_done(a,255)


                    # time.sleep(0.1)

    except KeyboardInterrupt:
        print("id not exist", end="\r")
        return None

def print_percent_done(index, total, bar_len=50, title='Please wait'):
    '''
    index is expected to be 0 based index.
    0 <= index < total
    '''
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = '█'*int(done)
    togo_str = '░'*int(togo)

    print(f'\t⏳{title}: [{done_str}{togo_str}] {percent_done}% done', end='\r')

    if round(percent_done) == 100:
        print('\t✅')
monitor_one_id(0x15b)

# r = 50
# for i in range(r):
#     print_percent_done(i,r)
#     time.sleep(.02)

