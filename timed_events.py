import time
import threading
import datetime
import sys
import os


shutdown_event = threading.Event()

def dowork():
    while not shutdown_event.is_set():
        print(datetime.datetime.now() ,end="\r")
        time.sleep(2.0)

def wor():
    while not shutdown_event.is_set():
        print(F"new_time {datetime.datetime.now()}" , end="\r")
        time.sleep(0.01)

# def main():

t = threading.Thread(target=dowork, args=(), name='worker')
t.start()

print("Instance started")

while 1:
    try:
        pass
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


# if __name__ == '__main__':
#     main()